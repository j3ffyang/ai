a = input("Give the 1st binary string: ")
b = input("Give the 2nd binary string: ")

y = int(a,2) ^ int(b,2)

print("The result is: ")
print(bin(y)[2:].zfill(len(a)))
# print('{0:b}'.format(y))
