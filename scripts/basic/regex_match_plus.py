import re

pattern = r"g+"

# '+' = {1,}

if re.match(pattern, "g"):
    print("match 1")

if re.match(pattern, "gggggggggg"):
    print("match 2")

if re.match(pattern, "abc"):
    print("match 3")