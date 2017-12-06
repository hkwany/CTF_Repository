#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
from Crypto.Util.number import size, long_to_bytes, bytes_to_long
from Crypto.Cipher import DES
from hashlib import sha512
import hashlib
from os import urandom

from pwn import *
import itertools
import time

fuzzing = "abcdefghijklmnopqrstuvwxyz0123456789QWERTYUIOPASDFGHJKLZXCVBNM"
fuzz = itertools.permutations(fuzzing, 5)
context.log_level = "debug"

k = 2048
key = "abcdefg1"

def pi_b(x, m):

	enc = DES.new(key)
	if m:
		method = enc.encrypt
	else:
		method = enc.decrypt
	s = long_to_bytes(x)
	sp = [s[a:a+8] for a in xrange(0, len(s), 8)]
	r = ""
	for a in sp:
		r += method(a)
	return bytes_to_long(r)


def get_bit(number, n_bit, dire):
	
	if dire:
		sn = size(number)
		if sn % 8 != 0:
			sn += (8 - sn % 8)
		return number >> (sn-n_bit)
	else:
		return number & (pow(2, n_bit) - 1)

def md5_proof(fuzz, salt, verify):
	y = len(verify)
	while True:
		try:
			padd = "".join(fuzz.next())
		except StopIteration:
			break
		if hashlib.md5(salt + padd).hexdigest().startswith("0000"):
			return padd

def verify(r):
	salt = r.readline()
	salt = salt.decode('base64')
	t1 = time.time()
	proof = md5_proof(fuzz, salt, "0000")
	print time.time() - t1
	r.send(proof.encode('base64'))



#def judge():

def main():
	r = remote("118.31.18.75",20013)
	# r = process("rsa2.py")
	verify(r)


	r.readuntil("n: ")
	n = r.readline().strip()
	print '----------------------------'

	print n
	print '----------------------------'
	n=r.recvuntil('\n', drop=True)
	r.readuntil("e: ")
	#r.recvuntil('\n', drop=True)
	e = r.readline().strip()
	r.readuntil("c: ")
	c=r.recvuntil('\n', drop=True)
	print '----------------------------'
	r.readuntil("u: ")
	u=r.recvuntil('\n', drop=True)


	print "n: ", n
	print "e: ", e
	print "c: ", c
	print "u: ", u
	print '----------------------------'
	r.readuntil("x: ")
	x = "1111"
	r.sendline(x)
	r.readuntil("y: ")
	y = "0002222000"
	r.sendline(y)
	
	r.close()

if __name__ == '__main__':
	# n = 0
	# for x in xrange(100):
	# 	if main():
	# 		n += 1

	# print "n: {}%".format(n)
	main()





'''



import socket
import base64
import hashlib
import random
import string
import sys
from zio import *

buf_len = 1024
sock = zio(("118.31.18.75",20013))

ret_bytes = sock.readline().strip()
sock.read_until("show me your work:")
salt = base64.decodestring(ret_bytes)
ans = ""
while True:
    i = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
    if hashlib.md5(salt + i).hexdigest().startswith("0000"):
        ans = i
        break

print ans
sock.write(base64.encodestring(ans))
sock.read_until("checked")
sock.readline()

n_str = sock.readline().strip()[5:][:-1]
e_str = sock.readline().strip()[5:]
c_str = sock.readline().strip()[5:][:-1]
u_str = sock.readline().strip()[5:][:-1]


sock.read_until("x:")
sock.write("\n")

sock.read_until("y:")
#send y
sock.write(u_str + "\n")

s_str = sock.readline().strip()[5:][:-1]

n = int(n_str, 16)
e = int(e_str, 16)
cipher = int(c_str, 16)
half_cipher = int(u_str, 16)
s = int(s_str, 16)

sock.close()


print (n, e, cipher, half_cipher, s)




'''

n = 0x5f00052ffdba441253cbec6d023ad3069e988ef20d36c775109245ac29854f700ceec615859adff96848fd1046ad239d437b575ed4ebdf339bbaaa9d8ef4812bfcaea8b70c3efd4d7b5597f5d187675d84273930d4d1c7bcc43bb8ceef13837daaedcb9f161a723e3cdb7ecf5f0e4a85bc9a807bcbada640f1e1439c712057bc694bc6b967e99e398b80789cfe6d10da2481df5bb486c1c4713adc4baffd2cccdfde7c48370a2164d29c0c87de22cec1a34e0eb5c8707e630e2abafb03e5c8e0da90ecbc51088e91c50e4658fecdeab34994b3791b7ca59f7c51bf57bd380117bb57f0c802532dbe820ae4b9260a90bf3107db4ebed213748dc8e6e09d052125L
p_fake = 0xab029d6351d3989b0d6d3ef693bb24131abbe15bb2aae1430ccfe2816a092ed1f2b9efd01895891112304dbf08fbf3f1d32cb57fc813ad09b4511752e8aca6d4781c3d3728ab16L
 
 
 
 
pbits = 1024
kbits = 456
pbar = p_fake & (2^pbits-2^kbits)
print "upper %d bits (of %d bits) is given" % (pbits-kbits, pbits)
 
PR.<x> = PolynomialRing(Zmod(n))
f = x + pbar
 
x0 = f.small_roots(X=2^kbits, beta=0.4)[0]  # find root < 2^kbits with factor >= n^0.3
print x0 + pbar

'''



n = 0x5f00052ffdba441253cbec6d023ad3069e988ef20d36c775109245ac29854f700ceec615859adff96848fd1046ad239d437b575ed4ebdf339bbaaa9d8ef4812bfcaea8b70c3efd4d7b5597f5d187675d84273930d4d1c7bcc43bb8ceef13837daaedcb9f161a723e3cdb7ecf5f0e4a85bc9a807bcbada640f1e1439c712057bc694bc6b967e99e398b80789cfe6d10da2481df5bb486c1c4713adc4baffd2cccdfde7c48370a2164d29c0c87de22cec1a34e0eb5c8707e630e2abafb03e5c8e0da90ecbc51088e91c50e4658fecdeab34994b3791b7ca59f7c51bf57bd380117bb57f0c802532dbe820ae4b9260a90bf3107db4ebed213748dc8e6e09d052125L
p_fake = 25469341510015610710601677541490068882874022771473379147959682877979811860690835905177575433486769235926750944378553837429714908846121392087707617153368450157831411033840331452402635316893579428297241392591768100008774205252294780519995317089863801331600746389471563346749402400584048767782402832414560955794979239140648096754408560344380360521300295416056532504527346890878830708030202503589314586128121926254376071861981570648841288044240102936057199541504839050994656267226010545841307490110261343492485615893311098351703701000220286503350522201318815497988460167971677642567134161349144833221240627311534482202273L
 
 
 
 
pbits = 2048
kbits = 900
pbar = p_fake & (2^pbits-2^kbits)
print "upper %d bits (of %d bits) is given" % (pbits-kbits, pbits)
 
PR.<x> = PolynomialRing(Zmod(n))
f = x + pbar
 
x0 = f.small_roots(X=2^kbits, beta=0.4)[0]  # find root < 2^kbits with factor >= n^0.3
print x0 + pbar




n=0x5f00052ffdba441253cbec6d023ad3069e988ef20d36c775109245ac29854f700ceec615859adff96848fd1046ad239d437b575ed4ebdf339bbaaa9d8ef4812bfcaea8b70c3efd4d7b5597f5d187675d84273930d4d1c7bcc43bb8ceef13837daaedcb9f161a723e3cdb7ecf5f0e4a85bc9a807bcbada640f1e1439c712057bc694bc6b967e99e398b80789cfe6d10da2481df5bb486c1c4713adc4baffd2cccdfde7c48370a2164d29c0c87de22cec1a34e0eb5c8707e630e2abafb03e5c8e0da90ecbc51088e91c50e4658fecdeab34994b3791b7ca59f7c51bf57bd380117bb57f0c802532dbe820ae4b9260a90bf3107db4ebed213748dc8e6e09d052125L
#p=0xBCF6D95C9FFCA2B17FD930C743BCEA314A5F24AE06C12CE62CDB6E8306A545DE468F1A23136321EB82B4B8695ECE58B763ECF8243CBBFADE0603922C130ED143D4D3E88E483529C820F7B53E4346511EB14D4D56CB2B714D3BDC9A2F2AB655993A31E0EB196E8F63028F9B29521E9B3609218BA0000000000000000000000000

p=0xab029d6351d3989b0d6d3ef693bb24131abbe15bb2aae1430ccfe2816a092ed1f2b9efd01895891112304dbf08fbf3f1d32cb57fc813ad09b4511752e8aca6d4781c3d3728ab16000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for i in xrange(0,0xff):

    p = p+0x10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    
    p_fake = p + 0x10000000000000000000000000
    pbits = 1024
    kbits = pbits-576
	pbar = p_fake & (2^pbits-2^kbits)
	print "upper %d bits (of %d bits) is given" % (pbits-kbits, pbits)
	PR.<x> = PolynomialRing(Zmod(n))
	f = x + pbar
	try:

		x0 = f.small_roots(X=2^kbits, beta=0.4)[0]  # find root < 2^kbits with factor >= n^0.4
		print x0 + pbar
		print '================================================================================'
	except:
		print i

		continue