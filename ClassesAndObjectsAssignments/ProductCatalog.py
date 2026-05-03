class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def add_stock(self, stock):
        self.stock += stock

    def sell(self, quantity):
        if self.stock < quantity:
            print("Not enough quantity")
            return
        self.stock -= quantity

p = Product("Laptop", 70000, 5)
p.sell(2)
print(p.stock)