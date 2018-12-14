import re

# Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1
# refers to the first group's subexpression, which is the matched
# expression itself, and not the regex pattern.

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print("match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("match 2")

match = re.match(pattern, "abc cde")
if match:
    print("match 3")

