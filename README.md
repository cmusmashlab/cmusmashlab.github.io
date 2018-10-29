## Quick Reference
- **Updating profile**: `_data/members.yml`
- **Adding publications**: `_publications/paper_name.yml`

The BibTeX and citation should be copied verbatim from the ACM DL, if possible.
Thumbnail pictures should be 16x9, at least 300 px wide.

## Updating profile
#### Edit Metadata
Modify `_data/members.yml`. 
Fields:
- `id`: This should be your last name. This is what you'll use throughout the site to refer to you. If you have a website listed, it will replace references of your name with a link to your website.
- `name`: Full name
- `image`: Path to your profile picture. Images should be square and ideally 165x165px.
- `website`: Full link to your personal website
- `affiliation`: Either HCII, ISR or SCS. See _data/affiliations.yml for details and to make modifications.
- `status`: One of `current`, `alumni`, `master_alumni`, `ugrad_alumni`, or `summer_alumni`
- `degree`: Free text. Suggested values: 'Ph.D. Student', 'Masters Student', 'Undergraduate'

#### Upload image
Images should be uploaded to `images/members/`. Images should be square and (ideally) 165x165px. If you upload something else, it will be cropped.

## Adding Publication
Create a new file in `_publications/`. I recommend copying an existing file (such as `eyecontact.md`).

- `authors`: This should be a list of full names. If an author is a lab member (or former lab member), use the member's `id` instead of their name to link it to their website.
- `award`: Should be either '', 'Best Paper Award', or 'Honorable Mention Award'.
- `bibtex`: Copy from the ACM DL, not from Google.
- `caption`: This will go under the image on the project detail page.
- `citation`: Copy from the ACM DL, not from Google.
- `conference`: This should be in the format: ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp), 2011
- `date`: Publication/presentation date
- `image`: Hi res image for the project detail page (accompanies `caption`). Add to `images/pubs/`.
- `news`: (optional) List of different press releases, which contains
	- `name`: the name of the news entity
	- `url`: the url to the article
	- `headline`: the headline
	- `date`: the date the article was published
- `pdf`: Copy from the ACM DL, not anywhere else.
- `thumbnail`: Must be 16x9 and 300px wide. Add to `images/pubs/`.
- `title`: Verbatim paper title
- `video`: (optional) Link to external video, such as YouTube or Vimeo.
- `video_embed`: (optional) HTML embed code for video player


## Scraping the ACM DL
If your paper is published by the ACM, you can create most of this metadata automatically using `resources/process_bibtex.py`. Edit the BibTeX at the end of the file and run it. It will download the PDF and create the markdown file for you.

## Local Development

1. Install Ruby if not already installed (installed by default on OS X). On Windows, use http://rubyinstaller.org/. On Linux, run `sudo apt-get install ruby-full`. This should come with the gem package manager.
2. Install Jekyll and plug-ins in one fell swoop. `gem install github-pages` (OS X users may need to `sudo gem install github-pages`) This mirrors the plug-ins used by GitHub Pages on your local machine including Jekyll, Sass, etc.
3. Clone down your fork `git clone git@gitlab.cs.washington.edu:ubicomplab/ubicomplab.github.io.git`
4. Serve the site and watch for markup/sass changes `jekyll serve`
5. View your website at http://127.0.0.1:4000/
6. Commit any changes and push everything to the master branch of your GitHub user repository. GitHub Pages will then rebuild and serve your website.
