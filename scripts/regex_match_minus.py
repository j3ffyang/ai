import re

pattern = r"ice(-)?cream"

# - means "zero or one repetitions"
# match both 'color' and 'colour'
# pattern = r"colo(u)?r"

if re.match(pattern, "ice-cream"):
    print("match 1")

if re.match(pattern, "icecream"):
    print("match 2")

if re.match(pattern, "sausages"):
    print("match 3")

if re.match(pattern, "ice--ice"):
    print("match 4")