import re

s = "Python"
if re.match(r'^[A-Z]', s):
    print("Starts with a capital letter.")