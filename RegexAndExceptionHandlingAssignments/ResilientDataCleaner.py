import re

text = "Na#me: A$le%x"

try:
    cleaned = re.sub(r'[^a-zA-Z0-9: ]', '', text)
    print(f"Cleaned Data: {cleaned}")
except:
    pass