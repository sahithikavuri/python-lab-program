class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

p = Product("Pen", 10, 5)
print(p.name, p.amount, p.price)
