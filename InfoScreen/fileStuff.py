def findLines(fileName,inString, leeway=2):
	f=open(fileName,'r')
	output=list()
	for line in f:
		if(inString in line[0:len(inString)+leeway]):
			output.append(line)
	f.close()
	return output

def fileContains(fileName,inString):
	f=open(fileName,'r')
	for line in f:
		if(inString in line):
			f.close()
			return True
	f.close()
	return False

def replaceIn(fileName,find,replacement):
	pass

def htmlList(lst):
	return ''.join(map((lambda val: "<li>"+str(val)+"</li>\n"),lst))
