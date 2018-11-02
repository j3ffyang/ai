# while operator
var = 1
while var <= 7:
    print(var)
    var = var + 1
"""print("End")"""

# break the loop
var1 = 3
while 4 == 4:
    print(var1)
    var1 = var1 + 1
    if var1 >= 10:
        print("Stop")
        break

# continue stops current iteration
var2 = 1
while True:
    var2 = var2 + 1
    if var2 == 5:
        print("skipping 5")
        continue
    if var2 == 10:
        print("stop")
        break
    print(var2)
