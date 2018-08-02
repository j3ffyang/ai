def pure_func(x, y):
    tmp = x + 2 * y
    return tmp
#    return tmp / (2 * x + y)

list=[]
def impure_func(arg):
    list.append(arg)
    return list

print(pure_func(2, 2))
print(pure_func(2, 2))
print(pure_func(2, 2))
print(pure_func(2, 2))

print(impure_func(2))
print(impure_func(2))
print(impure_func(2))
print(impure_func(2))