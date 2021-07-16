s = 'PyvragFvqrYbtvafNerRnfl@syner-ba.pbz'
flag = ''

# 四种情况：
# 原字符小写：
#     - 新字符 = 原字符 + 13
#     - 新字符 = 原字符 + 13 - 25
# 原字符大写：
#     - 新字符 = 原字符 + 13
#     - 新字符 = 原字符 + 13 - 25

for c in s:
    if (ord(c) - 13) >= 65 and ord(c) <= 90:
        flag += chr(ord(c) - 13)
    elif (ord(c) + 26 - 13) >= 65 and (ord(c) + 26 - 13) <= 90 and (ord(c) + 26) > 90:
        flag += chr(ord(c) - 13 + 26)
    elif (ord(c) - 13) > 96 and ord(c) <= 122:
        flag += chr(ord(c) - 13)
    elif (ord(c) + 26 - 13) > 96 and (ord(c) + 26 - 13) <= 122 and (ord(c) + 26) > 122:
        flag += chr(ord(c) - 13 + 26)
    else:
        flag += c

print(flag)