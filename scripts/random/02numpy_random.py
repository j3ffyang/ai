# https://machinelearningmastery.com/introduction-to-random-number-generators-for-machine-learning/

# demo the numpy psudorandom num gen 
from numpy.random import seed
from numpy.random import rand 

# seed the gen 
seed(7)
print(rand(5))

# seed the gen to get the same sequence 
print("Reseeded")
seed(7)
print(rand(5))
