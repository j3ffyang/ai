def test(func, arg):
    return func(func(arg))

def mult(x):
    return x * x

print(test(mult, 2))