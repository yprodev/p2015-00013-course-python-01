name = raw_input("Enter file:")

if len(name) < 1 : name = "data/work_with_files/mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle :
	line = line.rstrip()
	if line.startswith('From ') :
		newLine = line.split(' ')
		newEmail = newLine[1]
		counts[newEmail] = counts.get(newEmail, 0) + 1

theMail = None
theBiggest = None

for mail, count in counts.items() :
	if theBiggest is None or count > theBiggest :
		theMail = mail
		theBiggest = count

print theMail, theBiggest
