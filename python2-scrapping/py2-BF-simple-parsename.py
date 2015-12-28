# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

count = raw_input('count -')
if len(count) < 1 : count = 4

position = raw_input('position -')
if len(position) < 1 : position = 3


for i in range(0, count, 1) :

	if len(url) < 1 : url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'

	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	# Retrieve all of the anchor tags
	listing = list()
	tags = soup('a')

	for tag in tags :
		urlName = tag.get('href', None)
		listing.append(urlName)

	url = listing[position - 1]
	print 'Retrieving: ', url





