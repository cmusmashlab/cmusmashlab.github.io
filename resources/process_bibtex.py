import bibtexparser
from slugify import slugify
import os
import frontmatter
import yaml
from yaml.representer import SafeRepresenter
import pylev
import requests
from bs4 import BeautifulSoup
import shutil

def change_style(style, representer):
    def new_representer(dumper, data):
        scalar = representer(dumper, data)
        scalar.style = style
        return scalar
    return new_representer


class folded_str(str): pass
class literal_str(str): pass

# represent_str does handle some corner cases, so use that
# instead of calling represent_scalar directly
represent_folded_str = change_style('>', SafeRepresenter.represent_str)
represent_literal_str = change_style('|', SafeRepresenter.represent_str)

yaml.add_representer(folded_str, represent_folded_str)
yaml.add_representer(literal_str, represent_literal_str)

# exported from http://dl.acm.org/author_page.cfm?id=81100490064
BIBFILE = "shwetak_acm.bib"
REF_URL = 'http://dl.acm.org/exportformats.cfm?id={0}&expformat=acmref'
PAPER_URL = 'http://dl.acm.org/citation.cfm?id={0}&preflayout=flat'
s = requests.Session()
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def load_author_list():
    author_list = {}
    with open(os.path.join('.', '..', '_data', 'members.yml')) as file:
        data = yaml.load(file)
        for member in data:
            author_list[member['name']] = member['id']
    return author_list

author_list = load_author_list()


def get_keyword_from_title(title):
    if ':' in title and title.index(':') < 30:
        title_part = title[0:title.index(':')]
    else:
        title_part = ' '.join(title.split(' ')[0:2])

    return slugify(title_part)


def link_author(author):
    global author_list
    for lab_author in author_list.keys():
        if pylev.levenshtein(lab_author, author)/max(len(lab_author), len(author)) < .30:
            return author_list[lab_author]
    return author


def fix_authors(authors_str):
    authors = authors_str.replace('\n', ' ').split(' and ')
    authors_fixed = []
    for author in authors:
        first_last = author.split(',')
        author_fixed = first_last[1].strip() + " " + first_last[0].strip()

        authors_fixed.append(link_author(author_fixed))
    return authors_fixed


def get_acm_ref(doi):
    ref_url = REF_URL.format(doi)
    r_ref = s.get(ref_url, headers=headers)
    soup = BeautifulSoup(r_ref.content, 'html.parser')
    for div in soup.find_all('div') + soup.find_all('script') + soup.find_all('a'):
        div.decompose()
    ref = soup.text.strip()
    return ref

conferences = {"UbiComp": "ACM International Joint Conference on Pervasive and Ubiquitous Computing",
               "ISWC": "ACM International Symposium on Wearable Computers",
               "CHI": "Conference on Human Factors in Computing Systems",
               "UIST": "ACM Symposium on User Interface Software and Technology",
               "Pervasive": "International Conference on Pervasive Computing",
               "PERVASIVE": "International Conference on Pervasive Computing",
               "BodyNets": "International Conference on Body Area Networks",
               "BODYNETS": "International Conference on Body Area Networks",
               "MobiCom": "ACM Annual International Conference on Mobile Computing and Networking",
               "CCS": "ACM Conference on Computer and Communications Security"}


def format_conf_name(conf):
    conf = conf.strip()
    if '\'' in conf:
        format = "{} ({}), {}"
        name, year = conf.split('\'')
        name = name.strip()
        if name in conferences.keys():
            return format.format(conferences[name], name, "20"+year)
        return conf
    return conf


def parse(entry, bibtex):
    title = get_keyword_from_title(entry['title'])
    # if os.path.exists(os.path.join('files', title + '.md')):
    #     return
    template = frontmatter.load('template.md')

    template['bibtex'] = literal_str(bibtex)
    template['title'] = entry['title']
    template['authors'] = fix_authors(entry['author'])

    doi = entry['acmid']

    template['citation'] = literal_str(get_acm_ref(doi))

    url = PAPER_URL.format(doi)
    r = s.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')
    pdf_a = soup.find('a', {'name': 'FullTextPDF'})
    abstract = soup.find('a', {'name': 'abstract'}).parent.nextSibling.nextSibling.text.strip()
    template['abstract'] = literal_str(abstract)

    date = soup(text="Publication Date")[0].parent.nextSibling.contents[0].strip()
    conference = soup(text="Title")[0].parent.parent.find("a").text
    if "table of contents" in conference.replace("\xa0", " "):
        conference = soup(text="Title")[0].parent.parent.find_all("td")[1].text.strip().split(" ")[0]
    template['conference'] = format_conf_name(conference)
    template['date'] = date
    if pdf_a is not None:
        pdf_link = pdf_a['href']
        pdf_url = 'http://dl.acm.org/'+pdf_link
        r_pdf = s.get(pdf_url, headers=headers, stream=True)
        with open(os.path.join('pdfs', title+'.pdf'), 'wb') as f:
            shutil.copyfileobj(r_pdf.raw, f)

        template['pdf'] = '/pdfs/{}.pdf'.format(title)


    with open(os.path.join('files', title + '.md'), 'w') as file:
        frontmatter.dump(template, file, Dumper=yaml.Dumper)
    print(title)


def is_valid(entry):
    return 'booktitle' in entry and \
           'adjunct' not in entry['booktitle'].lower() and \
           'extended abstracts' not in entry['booktitle'].lower()

def parse_bibtex(bib_str):
    bib_database = bibtexparser.loads(bib_str)
    for (entry, bibtex) in zip(bib_database.entries, bib_str.split('\n\n')):
        if is_valid(entry):
            parsed = parse(entry, bibtex)

def run():

    URL = "http://dl.acm.org/citation.cfm?id=2971653"
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

    r = s.get(URL, headers=headers)

    with open(BIBFILE, 'r') as bibfile:
        bib_str = bibfile.read()

    parse_bibtex(bib_str)


if __name__ == "__main__":
    bib = """@inproceedings{Froehlich:2012:DEP:2207676.2208397,
 author = {Froehlich, Jon and Findlater, Leah and Ostergren, Marilyn and Ramanathan, Solai and Peterson, Josh and Wragg, Inness and Larson, Eric and Fu, Fabia and Bai, Mazhengmin and Patel, Shwetak and Landay, James A.},
 title = {The Design and Evaluation of Prototype Eco-feedback Displays for Fixture-level Water Usage Data},
 booktitle = {Proceedings of the SIGCHI Conference on Human Factors in Computing Systems},
 series = {CHI '12},
 year = {2012},
 isbn = {978-1-4503-1015-4},
 location = {Austin, Texas, USA},
 pages = {2367--2376},
 numpages = {10},
 url = {http://doi.acm.org/10.1145/2207676.2208397},
 doi = {10.1145/2207676.2208397},
 acmid = {2208397},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {eco-feedback, iterative design, sustainability, water},
}"""
    parse_bibtex(bib)
    #run()