from src.base_product import BaseProduct


# Class Product
class Product(BaseProduct):
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
        if quantity and quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    def __call__(self, *args, **kwds):
        return f"{self.name}, харрактеристики: {self.description}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, products):
        if isinstance(products, self.__class__):
            sum_income_items = self.__price * self.quantity
            result = products.price * products.quantity
            result += sum_income_items
            return result
        else:
            print("Переданный объект не является экземпляром класса Product\n")

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


class MixinLog(Product):
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        print(
            f"""  Был создан экземпляр класса {str(self.__class__)[20:-2]}
        Входные данные:
            Наименование: {self.name}
            Описание: {self.description}
            Цена: {self.price}
            Колличество: {self.quantity}"""
        )


class Smartphone(MixinLog, Product):

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, item):
        if type(item) is self.__class__:
            return super().__add__(item)
        else:
            raise TypeError("Invalid type")


class LawnGrass(MixinLog, Product):

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, item):
        if type(item) is self.__class__:
            return super().__add__(item)
        else:
            raise TypeError("Invalid type")
