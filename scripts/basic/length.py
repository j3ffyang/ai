
# What'll be the output?

class String(str):

    def __init__(self, val):
        self.value = val
        self.length = len(val)


obj = String('Inheritance in Python')

print(len(obj.split('in')[-1]))
