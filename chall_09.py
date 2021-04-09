from pwn import *
binary=ELF("./chall_09")
p=process("./chall_09")
p.sendline(xor(binary.string(binary.sym.key),"\x30"))
p.interactive()
