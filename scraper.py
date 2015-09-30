# make all these stuff into a function for pulitzer winners (left column) 
# ohohohohohohohohohohoh! 

import requests
from bs4 import BeautifulSoup 
import csv
import time
import re

# turn all Journalism urls into a list 
url = "http://www.pulitzer.org/bycat"		
r = requests.get(url)
soup = BeautifulSoup(r.content) 


links = soup.find("div", {"id": "awards_center"}).find_all("a") #Journalism category only 
urls = [] #a list of urls of sub-categories of Journalism 

for link in links:
	if "/bycat/" in str(link):
		notag_link= re.findall(r'"([^"]*)"', str(link)) #remove tag <a href=..... 
		almost_clean_link = str(notag_link) 
		clean_link='http://www.pulitzer.org'+ almost_clean_link[2:-2] #remove [' and ']
		urls.append(clean_link)
#print urls 

print len(urls)

# make winners of pulitzer in each url into a .csv file 
def WinnertoCSV(url):
	
	category = url.split('/') 
	category_name = category[len(category)-1] #get category name

	r = requests.get(url)
	soup = BeautifulSoup(r.content) 
	winner_list = []
	left_div = soup.find("div", {"class": "left"})

	if left_div is None:
		print "Couldn't find left div on", url
		return

	for journalist in left_div.find_all("div", {"class": "item"}):

		c_title = journalist.find( "div", {"class":"citation-heading"});
		year = c_title.find("span", {"class": "year"}).text
		#print year 

		if c_title.find("span", {"class", "title"}):
			title = c_title.find("span", {"class", "title"}).text
		
		else:
			title = "None"
		#print title

		if c_title.find("span", {"class","publication"}):
			publication = c_title.find("span", {"class","publication"}).text 

		else:
			publication = "None"
		#print publication

		#print year_list, title_list, publication_list
		winner = { 'year': int(year), 'name': str(title), 'publication': str(publication), 'category': category_name}
		winner_list.append(winner)

	#return winner_list #a list of dict
	
	keys =winner_list[0].keys()
	timestamp = str(int(time.time())) #to create different files 
	filename = category_name + timestamp +'.csv'

	with open(filename, 'wb') as output_file:
	    print 'writing to', filename
	    dict_writer = csv.DictWriter(output_file, fieldnames=['category','year', 'name', 'publication']) #assign header
	    dict_writer.writeheader()
	    dict_writer.writerows(winner_list)

	return output_file

for u in urls[29:30]: #urls[29:30] means last item in list 
#	print u
	WinnertoCSV(u)
