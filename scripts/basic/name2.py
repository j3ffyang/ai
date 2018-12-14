import sys

# def convert("file_path"):
with open("name.txt", "r") as f:
    data_array = f.readlines()
    for data in data_array:
        # remove \n
        data = data.strip()
        print('"' + data + '",')
        # print("\"%sa\";" % (data))

# with write("name_proc.json", "w"):

# if __name__ == "__main__":
#    file_path = sys.argv[1]
#    convert(file_path)