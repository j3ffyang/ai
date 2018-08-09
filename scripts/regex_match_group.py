import re

pattern = r"a(bc)(de)(f(g)h)i"

# g = group(4)
# eg, in 1(23)(4(56)78)9(0) -> group(3) = 56

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.groups())
