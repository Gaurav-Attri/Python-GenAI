import re

name = "Alex"
email = "alex@corp.com"
phone = "9876543210"

try:
    if not re.match(r'^[A-Za-z]+$', name):
        raise ValueError("Invalid name")
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValueError("Invalid email")
    if not re.match(r'^\d{10}$', phone):
        raise ValueError("Invalid phone")
    print("Valid inputs.")
except Exception:
    print("Invalid input.")