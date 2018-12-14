def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
#    print("{0} - {1}%".format(char, round(perc,2)))

print(count_char(text, "r"))