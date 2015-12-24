import re

fileOne = 'data/regexp/regex_sum_214665.txt'

myFile = open(fileOne)

count = 0
finded = None
num = None
bigList = []

for line in myFile :
	line = line.rstrip()
	finded = re.findall('[0-9]+', line)
	if len(finded) < 1 : continue
	finded = map(int, finded)
	bigList = bigList + finded

bigSum = sum(bigList)
print bigSum


