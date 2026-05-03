try:
    result = 10 / 'a'
except ZeroDivisionError:
    print("Error: Division by zero.")
except TypeError:
    print("Error: Invalid input type.")