s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm' #off_418000
d = 'TOiZiZtOrYaToUwPnToBsOaOapsyS' #off_418004
flag = ''
for i in range(len(d)):
    if i % 2 == 0:
        flag = flag + d[i]
    else:
        if(d[i].isupper()):
            flag = flag + chr(s.find(d[i]) + 96)
        else:
            flag = flag + chr(s.find(d[i]) + 38)

print(flag)