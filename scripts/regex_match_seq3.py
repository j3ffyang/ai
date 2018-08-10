import re

pattern = r"\b(cat)\b"
# "\b(cat)\b" basically matches the word "cat" surrounded by word boundaries.

match = re.search(pattern, "The cat sat!")
if match:
    print("match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
#   print(match)
    print("match 2")

match = re.search(pattern, "We scattered.")
if match:
    print("match 3")