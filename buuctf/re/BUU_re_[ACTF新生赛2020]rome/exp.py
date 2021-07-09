model = [81, 115, 119, 51, 115, 106, 95, 108, 122, 52, 95, 85, 106, 119, 64, 108]
flag = ''
for k in range(0, 16):
    for i in range(0, 127):  
        z = i
        if i > 64 and i <= 90:
            i = (i - 51) % 26 + 65
        if i > 96 and i <= 122:
            i = (i - 79) % 26 + 97
        if(i == model[k]):
            flag += chr(z)

print(flag)