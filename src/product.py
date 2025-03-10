# Class Product
class Product:
    """Accepts 4 required properties and returns data using 4 methods:
    name - returns the name
    description - returns the product description
    price - returns the product price
    quantity - returns the product quantity
    """

    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, update: dict):
        result = []
        for i, key in enumerate(update):
            result.append(update[key])

        return Product(*result)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            if value < self.__price:
                user = input("""Новая цена ниже, вы уверены?\nВведите "Y"(yes) или "N"(no):\n""").upper()
                if user == "Y":
                    self.__price = value
                else:
                    print(f"Значение цены {value} не сохранено.")
            else:
                self.__price = value
        else:
            print("""Цена не должна быть "0" или отрицательная""")
