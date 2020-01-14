# reverse cipher 

message = 'Three can keep a secret, if two of them are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1
print(translated)

reversed = ""
m = len(translated) - 1
while m >= 0:
    reversed = reversed + translated[m]
    print(m, translated[m], reversed)
    m = m - 1
print(reversed)
