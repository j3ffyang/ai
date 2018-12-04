# https://www.dataquest.io/blog/numpy-tutorial-python/

import numpy as np 

# this is monthly earnings for 2 years
earnings= [
            [
                [500, 505, 490],
                [810, 450, 678],
                [234, 897, 439],
                [560, 1023,640]
            ], 
            [
                [600, 605, 490],
                [345, 900,1000],
                [780, 730, 710],
                [670, 540, 324]
            ]
           ]

earnings= np.array(earnings)
print(earnings[0,0,0])
print(earnings.shape)   # shape= (2,3,4)
print(earnings[:, 0, 0])    # all earnings for Jan for all years
