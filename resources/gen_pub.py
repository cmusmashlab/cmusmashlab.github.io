import yaml

# stream = file('../_publications/fitbyte.md','r')
# data = yaml.load_all(stream)
# for dat in data:
# 	print dat
# 	break

pub_data = {}
# pub_data['abstract'] = input ('Paste the paper abstract (make sure it is in a single paragraph:')
# stream = file('../_publications/test2.md','w')
# stream.write('---\n')
# yaml.dump(dat,stream)
# stream.write('---')
# stream.close()


#bibtex: create
#citation: create
#change options for all fields
#make changes to existing mds

def genBib():
	bibString = '@inproceedings{'+authorNames[0].split(' ')[1]+pub_data['year']+',\ntitle={'+pub_data['title']+'},\nauthor={'
	for author in authorNames:
		bibString = bibString+author+', '
	bibString = bibString+'},\n'
	bibString = bibString+'booktitle={'+pub_data['conference']+'},\n'
	bibString = bibString + 'year={'+pub_data['year']+'}\n}'

	return bibString

def genCite():
	citeString = ''
	count = 0

	for author in authorNames:
		citeString = citeString+author
		if count==len(authorNames)-1:
			citeString = citeString+'. '
		else:
			citeString = citeString+','

		count=count+1
	
	citeString = citeString + pub_data['year'] + '. '+pub_data['title']+'. '+pub_data['conference']+'.'
	print (citeString)
	return citeString

def editPaperTitle():
	return input ('Enter full paper title: ')

def editPaperVenue():
	conferences = {"IMWUT": "Proceedings of the ACM on Interactive, Mobile, Wearable, and Ubiquitous Technologies (IMWUT)",
               "ISWC": "Proceedings of the ACM International Symposium on Wearable Computers (ISWC)",
               "CHI": "Proceedings of the Annual ACM Conference on Human Factors in Computing Systems (CHI)",
               "UIST": "Proceedings of the Annual ACM Symposium on User Interface Software and Technology (UIST)",
               }
	print ('Enter the name of the conference or journal below. If it is one of the places in this list, then you can use the short name too. No need to add the year right now.\n')
	for conference in conferences:
		print (conference)
	print('')

	venue = input()
	if venue in conferences:
		venue = conferences[venue]

	pub_data['conference'] = venue 

def editPaperYear():
	pub_data['year'] = input('Enter year (yyyy): ')

def editPaperMonth():
	return input('Enter month of publication (mm): ')


def editPaperDay():
	return input('Enter the day of the month when this paper will be published (dd): ')

def editPaperCategory():
	category = input('Enter the broad category that this paper belongs to (options: health, activity, interaction, accessibility).\nIf a paper belongs to multiple categories, separate categories by comma: ')
	category = "".join(category.split())
	return category


def editThumbnail():
	thumbnail = input('Enter the filename for the thumbnail (including extension).\nMake sure to also add the thumbnail file to /images/pubs/ folder: ')
	pub_data['thumbnail'] = '/images/pubs/'+thumbnail

def editMainImg():
	print('It is recommended to use a higher resolution image for the main display image.')
	print('If you still want to use the thumbnail as the main pic, press <Enter>.')
	print('Otherwise enter filename for the main image (include extension)')
	print('Make sure to also add the thumbnail file to /images/pubs/ folder.')
	imageFilename = input()
	if imageFilename == '':
		pub_data['image'] = pub_data['thumbnail']
	else:
		pub_data['image'] = '/images/pubs/'+imageFilename

def editPaperName(title):
	name = title.split(':')[0]


	print ('\nIs this the correct project title for this paper?\n'+name)
	isProjectNameFine = input('(y/n): ')

	if isProjectNameFine == 'n':
		name = input ('Enter the name of the project (if no specific name, press <enter>): ')

	if name == '':
		name = title
	return name

def editAuthorNames():
	print('Add authors (in the correct order):\n')
	name = 'blank'
	#read lab member ids from members.yml
	memberDataStream = open('../_data/members.yml')
	membersData = yaml.full_load(memberDataStream)
	dash = '-'*30
	authorCount = 1
	currentAuthorIDList=list()
	currentAuthorNameList = list()
	while len(name) > 0:
		print ('Current Smash Lab members:')
		print (dash)
		print('{:<10}{:<20}'.format('id','name'))
		print (dash)
		for member in membersData:
			if member['status'] == 'current' or member['status'] == 'shifu':
				print('{:<10}{:<20}'.format(member['id'],member['name']))
		
		authorMsg = '\nIf the author ' + str(authorCount) + ' is a member of Smash Lab and is in this list, enter their id, otherwise enter full name: '
		name = input(authorMsg)
		isMatchFound = False
		for tempMember in membersData:
			if tempMember['id']	== name:
				isMatchFound = True
				print('match Found')
				currentAuthorIDList.append(tempMember['id'])
				currentAuthorNameList.append(tempMember['name'])
				

		if isMatchFound == False:
			currentAuthorIDList.append(name)
			currentAuthorNameList.append(name)

		if name == '':
			print ('Final Author List:')
		else:
			print ('Author List:')
		print(', '.join(currentAuthorNameList))
		print('')
		authorCount = authorCount + 1

	return currentAuthorIDList,currentAuthorNameList
def editPDFLink():
	pdflink = input('Enter the filename for the paper PDF (including extension).\nMake sure to also add the PDF file to /pdfs/ folder: ')
	pub_data['pdf'] = '/pdfs/'+pdflink
	return pdflink

def editVideoID():
	videoID = input('Enter the video ID from YouTube. \nFor example, for BeamBand, the YouTube link is: https://www.youtube.com/embed/jhY4NsIW2kQ, \nbut all we need here is the suffix code (e.g., jhY4NsIW2kQ in this case).\nIf no video, press <Enter>: ')
	if len(videoID) > 0:
		pub_data['video'] = 'https://youtu.be/'+videoID
		pub_data['video_embed'] = '<iframe width="560" height="315" src="https://www.youtube.com/embed/'+videoID+'" frameborder="0" allowfullscreen></iframe>'

def editOneLiner():
	oneliner = input('Enter a one-liner about the paper.\nThis will be shown as a short blurb on the website. : ')
	pub_data['blurb'] = oneliner

def editHomepageStatus():
	if input('Do you want to display the paper on the homepage? (y/n) ') == 'y':
		pub_data['onhomepage'] = True
	else:
		pub_data['onhomepage'] = False

def editAwardStatus():
	award = input('If this paper has won any awards, please enter the name of the award here (otherwise press <Enter>) : ')
	if len(award) > 0:
		pub_data['award'] = award


def editAbstract():
	abstract = input('Enter the paper abstract here. Make sure to remove all newlines from the text. The abstract should be a single paragraph:\n')
	pub_data['abstract'] = abstract

def showChangeInterface():
	print ('Enter appropriate key for whatever you want to change:')
	print ('<1> Title')
	print ('<2> Project name.')
	print ('<3> Author list')
	print ('<4> Venue')
	print ('<5> Date')
	print ('<6> Thumbnail filename')
	print ('<7> Main image filename')
	print ('<8> Link to paper PDF')
	print ('<9> Video ID on YouTube')
	print ('<10> One-liner')
	print ('<11> Homepage status')
	print ('<12> Award status')
	print ('<13> Abstract')

	changeChoice = input('')

	if changeChoice == '1':
		pub_data['title'] = editPaperTitle()
	if changeChoice == '2':
		pub_data['name'] = editPaperName(pub_data['title'])
	if changeChoice == '3':
		authorIDs, authorNames =editAuthorNames()
		pub_data['authors'] = authorIDs
	if changeChoice == '4':
		editPaperVenue()
	if changeChoice == '5':
		editPaperDate()
	if changeChoice == '6':
		editThumbnail()
	if changeChoice == '7':
		editMainImg()
	showAllInfo()
	isAllFine = input('Does everything look good here? (y/n): ')

	if isAllFine == 'n':
		showChangeInterface()

def editPaperDate():
	editPaperYear()
	month = editPaperMonth()
	day = editPaperDay()
	pub_data['date'] = pub_data['year']+'-'+month+'-'+day

def showAllInfo():
	print (pub_data)

print('Congratulations on your new publication! We will now add information about the publication one by one.')
print('If anything is wrong, don\'t worry. You will have the opportunity to edit the information once we collect everything.')
print('If needed, you can also edit the .md file in _publications folder later. This script gets you started with populating the info.')

#paper title
print('-------\nTitle\n-------')
pub_data['title'] = editPaperTitle()


#project name
print('-------\nProject Name\n-------')
pub_data['name'] = editPaperName(pub_data['title'])


#paper category
print('--------\n Category\n------')
pub_data['category'] = editPaperCategory()

#authors
print('-------\nAuthors\n-------')
authorIDs, authorNames = editAuthorNames()

pub_data['authors'] = authorIDs

#venue
print('-------\nVenue\n-------')
editPaperVenue()

#date
print('-------\nDate\n-------')
editPaperDate()

#thumbnail
print('-------\nThumbnail\n-------')
editThumbnail()

#main image
print('-------\nMain Image\n-------')
editMainImg()

#link to paper
print('-------\nPDF\n-------')
pdfname = editPDFLink()

#video id on youtube
print('-------\nYouTube Link\n-------')
editVideoID()

#oneliner
print('-------\nOne line blurb\n-------')
editOneLiner()

#homepage
'-------\nOn homepage?\n-------'
editHomepageStatus()

#award
'-------\nAny award?\n-------'
editAwardStatus()

#abstract
'-------\nAbstract\n-------'
editAbstract()


showAllInfo()



isAllFine = input('Does everything look good here? (y/n): ')

if isAllFine == 'n':
	showChangeInterface()

genBib()
genCite()

pub_data['bibtex'] = genBib()
pub_data['citation'] = genCite()

mdFilePath = '../_publications/'+pdfname.split('.')[0]+'.md'
stream = open(mdFilePath,'w')
stream.write('---\n')
yaml.dump(pub_data,stream)
stream.write('---')
stream.close()
