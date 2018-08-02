from itertools import accumulate, takewhile

nums = list(accumulate(range(5)))
# nums = list(accumulate(0,1,2,3,4,5,6,7))
print(nums)
print(list(takewhile(lambda x:x<= 18, nums)))