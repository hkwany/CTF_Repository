import base64
file = open('flag','r')
#print file.read()
while 1:
	line = file.readline()
	if not line:
		break
	pass
	try:
		#print line
		flag = base64.b64decode(line)
		print flag 
	except:
		break