def test_class_product_1(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_class_product_2(product2):
    assert product2.name == "Xiaomi Redmi Note 11"
    assert product2.description == "1024GB, Синий"
    assert product2.price == 31000.0
    assert product2.quantity == 14


def test_class_category_1(category1):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category1.products != []


def test_class_category_2(category2):
    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category2.products != []


def test_count_category1(category1):
    assert category1.category_count == 3
    assert category1.product_count == 7


def test_count_category2(category2):
    assert category2.category_count == 4
    assert category2.product_count == 8
