class Flower:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

class Bouquet:
    def __init__(self):
        self.flowers = []
        self.price = 0

    def add_flower(self, flower, quantity):
        if quantity > flower.quantity:
            print(f"Not enough {flower.name} in stock.")
        else:
            self.flowers.append((flower, quantity))
            self.price += flower.price * quantity
            flower.quantity -= quantity

    def __str__(self):
        result = ""
        for flower, quantity in self.flowers:
            result += f"{quantity} {flower}\n"
        result += f"Total price: ${self.price:.2f}"
        return result

rose = Flower("Rose", 2.50, 10)
lily = Flower("Lily", 3.00, 15)
tulip = Flower("Tulip", 1.50, 20)

bouquet = Bouquet()
bouquet.add_flower(rose, 5)
bouquet.add_flower(lily, 10)
bouquet.add_flower(tulip, 8)

print(bouquet)

print(f"\n{rose.name} quantity: {rose.quantity}")
print(f"{lily.name} quantity: {lily.quantity}")
print(f"{tulip.name} quantity: {tulip.quantity}")
