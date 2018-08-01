
#### Document Objective
- Bitwise XOR of binary strings
- Convert the binary strings to an integer base 2, then XOR, then ```bin()``` and then skip the first two characters, ```0b```, hence the ```bin(y0)[2:]```. After that, just ```zfill``` to the length - ```len(a)```, for this case.

#### Document Reference
Credit > https://stackoverflow.com/questions/19414093/how-to-xor-binary-with-python

## Code

```python
a = input("Give the 1st binary string: ")
b = input("Give the 2nd binary string: ")

y = int(a,2) ^ int(b,2)

print("The result is: ")
print(bin(y)[2:].zfill(len(a)))
# print('{0:b}'.format(y))
```
