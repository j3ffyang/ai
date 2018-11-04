
def add(x, y):
    return x + y

def double(func, x, y):
    return func(func(x, y), func(x, y))

var1 = 7
var2 = 11

print(double(add, var1, var2))
