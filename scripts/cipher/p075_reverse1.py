
msg = '123'
trans = ''

i = len(msg) - 1

while i >= 0:
    trans = trans + msg[i]
    i = i - 1
print(trans)


rev = ''
j = len(trans) - 1

while j >= 0:
    rev = rev + trans[j]
    j = j - 1
print(rev)
