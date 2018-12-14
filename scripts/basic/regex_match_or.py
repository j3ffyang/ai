import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print("match 1")

match = re.match(pattern, "grey")
if match:
    print("match 2")

match = re.match(pattern, "griy")
if match:
    print("match 3")