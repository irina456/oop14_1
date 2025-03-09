from src.product import Product


class Category:
    """Accepts 3 required properties and returns data using 3 methods
    name - returns category name
    description - returns product description
    products - returns product list
    Has 2 attributes:
    category_count - returns number of categories
    product_count - returns number of products

    """

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __call__(self):
        result = ""
        for i, key in enumerate(self.__products):
            result += f"{key.name}, {key.price} руб. Остаток: {key.quantity} шт.\n"
        return result

    def __str__(self):
        result = 0
        for i, key in enumerate(self.__products):
            result += key.quantity
        return f"{self.name}, количество продуктов: {result} шт.\n"

    def add_product(self, new_item):
        if isinstance(new_item, Product):
            self.__products = [new_item]
        else:
            print(f"Объект {new_item} не является экземпляром класса Product\n")

    @property
    def products(self):
        result = ""
        for i, key in enumerate(self.__products):
            result += f"{key.name}, {key.price} руб. Остаток: {key.quantity} шт.\n"
        return result
