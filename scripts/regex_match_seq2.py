import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 9999!")

if match:
    print("match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("match 2")

match = re.match(pattern, "!$?")
if match:
    print("match 3")