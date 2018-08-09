import re

pattern = r"egg(spam)*"

# start with 'egg'
# * = repetition

if re.match(pattern, "egg"):
    print("match 1")

if re.match(pattern, "eggspamspamegg"):
    print("match 2")

if re.match(pattern, "spam"):
    print("match 3")