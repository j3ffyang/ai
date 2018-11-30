# https://stackoverflow.com/questions/43300179/plotting-an-array-in-python

file = open("maze.txt", 'r')
arr = []
for line in file.readlines():
    #print();
    arr1 = []
    for c in line:
        if(c.isspace() and (c!="\n")):
            arr1.append(1)
            #print("1",end="")
        elif(c!="\n"):
            arr1.append(0)
            #print("0",end="")

    arr.append(arr1)
#print()
#print(arr)
for row in arr:
    print(row)

import matplotlib.pyplot as plt

plt.pcolormesh(arr)
plt.axes().set_aspect('equal') #set the x and y axes to the same scale
plt.xticks([]) # remove the tick marks by setting to an empty list
plt.yticks([]) # remove the tick marks by setting to an empty list
plt.axes().invert_yaxis() #invert the y-axis so the first row of data is at the top
plt.show()
