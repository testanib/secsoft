from pwn import *
from Crypto.Util.number import *
import time

p=remote("167.172.231.203", 8888)
sleep(.2)
i = 0
while i <= 100:
    sleep(.3)
    resp=p.recv()
    print(resp)
    s1 = resp.find(b'g: ')
    s2 = resp.find(b" (format1")
    str1 = resp[s1+3:s2]
    s3 = resp.find(b"AND ")
    s4 = resp.find(b" (format2")
    str2 = resp[s3+4:s4]
    format1 = resp[resp.find(b"format1 ")+8:resp.find(b") AND")]
    format2 = resp[resp.find(b"format2 ")+8:resp.find(b") @@")]

    str1conv = str1
    str2conv = str2

    if format1.decode("utf-8") == "bytearray":
        str1conv = bytes(eval(str1))
    elif format1.decode("utf-8") == "hexdigest":
        str1conv = bytes.fromhex(str1.decode("utf-8"))
    elif format1.decode("utf-8") == "integer":
        str1conv = long_to_bytes(str1.decode("utf-8"))

    if format2.decode("utf-8") == "bytearray":
        str2conv = bytes(eval(str2))
    elif format2.decode("utf-8") == "hexdigest":
        str2conv = bytes.fromhex(str2.decode("utf-8"))
    elif format2.decode("utf-8") == "integer":
        str2conv = long_to_bytes(str2.decode("utf-8"))

    result = xor(str1conv,str2conv)
    p.sendline(result.decode("latin-1"))
    i += 1
