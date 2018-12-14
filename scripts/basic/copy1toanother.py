with open("file1.txt", "r") as readfile:
    with open("file2.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)
