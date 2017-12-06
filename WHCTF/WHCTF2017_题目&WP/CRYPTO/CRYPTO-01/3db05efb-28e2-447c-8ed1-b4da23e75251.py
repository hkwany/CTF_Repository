'''
from Crypto.Util.number import getPrime,long_to_bytes,bytes_to_long
import primefac
import time
from os import urandom
import hashlib
import sys
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)
import sys
sys.stdout = Unbuffered(sys.stdout)
def gen_args():
    p=getPrime(1024)
    q=getPrime(1024)
    n=p*q
    e=0x10001
    d=primefac.modinv(e,(p-1)*(q-1))%((p-1)*(q-1))
    return (p,q,e,n,d)
def proof():
    salt=urandom(4)
    print salt.encode("base64"),
    proof=raw_input("show me your work: ")
    if hashlib.md5(salt+proof.decode("base64")).hexdigest().startswith("0000"):
        print "checked success"
        return 1
    return 0

def run():
    if not proof():
        return
    m=int(open("/home/bibi/PycharmProjects/work/whctf/flag","r").read().encode("hex"),16)#flag{*}
    (p,q,e,n,d)=gen_args()
    c=pow(m,e,n)
    print "n:",hex(n)
    print "e:",hex(e)
    print "c:",hex(c)
    t=int(hex(m)[2:][0:8],16)
    u=pow(t,e,n)
    print "u:",hex(u)
    print "===="
    x=int(hex(m)[2:][0:8]+raw_input("x: "),16)
    print "===="
    y=int(raw_input("y: "),16)
    if (pow(x,e,n)==y and pow(y,d,n)==t):
        print "s:",hex(int(bin(p)[2:][0:568],2))
run()
'''
'''
a=0x10001
b=0x1
print a+b'''
'''

'''

'''
p=0xab029d6351d3989b0d6d3ef693bb24131abbe15bb2aae1430ccfe2816a092ed1f2b9efd01895891112304dbf08fbf3f1d32cb57fc813ad09b4511752e8aca6d4781c3d3728ab16000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for i in xrange(0,0xff):

    p = p+0x10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    
    p_fake = p + 0x10000000000000000000000000
    pbits = 1024
    kbits = pbits-576
   
    print hex(p_fake)
0x10000000000000000000000000



'''

'''


for i in xrange(0,0xff):
    p = int('ff19a56ff52369bd5648732f9efdc4226a0861637b5a141e34d25d6200c8f9af479167468160dbf6fb72a9219ab483f97b42e336854b48ba977d273414b03598931f1ad442e138' + str(hex(i))[2:] + '0' * (256 - 144), 16)
    p_fake = p+0x10000000000000000000000000
    pbits = 1024
    print hex(p_fake)
'''

'''

n=0x5f00052ffdba441253cbec6d023ad3069e988ef20d36c775109245ac29854f700ceec615859adff96848fd1046ad239d437b575ed4ebdf339bbaaa9d8ef4812bfcaea8b70c3efd4d7b5597f5d187675d84273930d4d1c7bcc43bb8ceef13837daaedcb9f161a723e3cdb7ecf5f0e4a85bc9a807bcbada640f1e1439c712057bc694bc6b967e99e398b80789cfe6d10da2481df5bb486c1c4713adc4baffd2cccdfde7c48370a2164d29c0c87de22cec1a34e0eb5c8707e630e2abafb03e5c8e0da90ecbc51088e91c50e4658fecdeab34994b3791b7ca59f7c51bf57bd380117bb57f0c802532dbe820ae4b9260a90bf3107db4ebed213748dc8e6e09d052125L
#p=0xBCF6D95C9FFCA2B17FD930C743BCEA314A5F24AE06C12CE62CDB6E8306A545DE468F1A23136321EB82B4B8695ECE58B763ECF8243CBBFADE0603922C130ED143D4D3E88E483529C820F7B53E4346511EB14D4D56CB2B714D3BDC9A2F2AB655993A31E0EB196E8F63028F9B29521E9B3609218BA0000000000000000000000000

p=0xab029d6351d3989b0d6d3ef693bb24131abbe15bb2aae1430ccfe2816a092ed1f2b9efd01895891112304dbf08fbf3f1d32cb57fc813ad09b4511752e8aca6d4781c3d3728ab16000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for i in xrange(0,0xff):

    p = p+0x10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    
    p_fake = p + 0x10000000000000000000000000
    print hex(p_fake)
    pbits = 1024
    kbits = pbits-576
    pbar = p_fake & (2^pbits-2^kbits)
    print pbar

'''





'''

0000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000L
0
'''


n=0xf76f573014ff063fe742985a6b5c7d79c1c81fb86a19342e910fd3922486568abd133e13eb7bbc25747ac6c5ead0f2b21a85fc76895e40d8b57b975e6c6cb1c5074e879325d030247d9d9bc63688cea0408f5508518f6ca2efee07fbe0fbe60a5efc16b8f7f415d2b223b8b5db6af2f84fc3045b7e355e7fa378e81d700116be0c31663e8368a9edad51114871b537ebc03afb0393a27b24fac194546c26ec8bd25c3f7efa28ee07e5e2e6f383750626b1ca74ca94f6237b1ec448423dc2b9771a4a86343f62382fc963282f30b8ae9764d49d6389bc46c51d4a251039fd2e2d921d95039daac58aca774970a8b90963f38720828e9799b629f9b49f0fbb8fbb
p=0xff19a56ff52369bd5648732f9efdc4226a0861637b5a141e34d25d6200c8f9af479167468160dbf6fb72a9219ab483f97b42e336854b48ba977d273414b03598931f1ad442e138
for i in xrange(0,0xff):
    p = int('ff19a56ff52369bd5648732f9efdc4226a0861637b5a141e34d25d6200c8f9af479167468160dbf6fb72a9219ab483f97b42e336854b48ba977d273414b03598931f1ad442e138' + str(hex(i))[2:] + '0' * (256 - 144), 16)
    p_fake = p+0x10000000000000000000000000
    print hex(p_fake)
    pbits = 1024
    kbits = pbits-576
    pbar = p_fake & (2^pbits-2^kbits)
    print pbar


