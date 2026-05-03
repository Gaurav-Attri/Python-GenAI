try:
    f = open("config.txt")
except FileNotFoundError:
    print("File not found. Creating a new file...")
    open("config.txt", "w")