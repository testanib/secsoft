from pwn import *
binary=ELF("./chall_17")
p=process("./chall_17")
from ctypes import *
#c_lib=ctypes.LoadLibrary('libc.so.6')
c_lib=cdll.LoadLibrary('libc.so.6')
c_lib.srand(c_lib.time(None))
p.sendline(str(c_lib.rand()))
print(p.recvuntil('\n'))
