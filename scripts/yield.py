#def countdown():
#    i = 5
#    while i > 0:
#        yield i
#        i -= 1
#
#for i in countdown():
#    print(i)

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))
