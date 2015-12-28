# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_214670.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
numberSum = 0
for tag in tags:
	# Look at the parts of a tag
	count = count + 1
	if (tag.get('class', None) == 'comments') :
		contentNum = int(tag.contents[0])
		numberSum += contentNum

print count
print numberSum