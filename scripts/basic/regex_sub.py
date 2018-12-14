import re

str = "My name is Jeff. Hi Jeff."
pattern = r"Jeff"
newstr = re.sub(pattern, "Grace", str)
print(newstr)