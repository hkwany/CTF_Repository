#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
b64c='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
f=io.open('1.txt','rb')
string=''
mark=0
while(1):
	stego_line=f.readline().replace('\n','')
	print stego_line
	if stego_line:
		mark=0
		normal_line=stego_line.decode('base64').encode('base64').replace('\n','')
		dnum=stego_line.count('=')
		length=len(normal_line)
		for i in range(length):
			if (stego_line[i]!=normal_line[i]):
				mark=1
				s1=bin(abs(b64c.index(stego_line[i])^b64c.index(normal_line[i])))[2:]
				dnum*=2
				len2=len(s1)
				while(1):
					if len2!=dnum:
						s1='0'+s1
						len2+=1
					else:
						break
				string+=s1
				
		if 	mark==0:
			string+='0'*(dnum*2)		
	else:
		break
len3=len(string)
len4=len3/8
len5=len3%8+1
for j in range(len5):
	string2=''
	for q in range(len4):
		i=q*8
		i+=j
		s=string[i:i+8]
		string2+=chr(int(s,2))
	print string2
f.close()
