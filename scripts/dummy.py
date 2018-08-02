with open("name.txt", "r") as readfile:
    with open("namex.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)
