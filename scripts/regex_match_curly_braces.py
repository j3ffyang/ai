import re

pattern = r"9{1,3}$"
# '+' = {1,}

if re.match(pattern, "9"):
    print("match 1")

if re.match(pattern, "999"):
    print("match 2")

if re.match(pattern, "9999"):
    print("match 3")