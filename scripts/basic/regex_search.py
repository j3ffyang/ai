import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("NM")

if re.search(pattern, "eggspamsausagespam"):
    print("M")
else:
    print("nm")

print(re.findall(pattern, "eggspamsausagespam"))
