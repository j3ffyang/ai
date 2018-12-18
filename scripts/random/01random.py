# https://machinelearningmastery.com/introduction-to-random-number-generators-for-machine-learning/

# demonstrates the python pseudorandom number generators
from random import seed
from random import random 

# seed the generators
seed(7)
for _ in range(5):
    print(random())

# seed the generators to get the same sequence
print("Reseeded")
seed(7)
for _ in range(5):
    print(random())
