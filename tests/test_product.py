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


def test_new_product(product4_new_product):
    new_product = product4_new_product
    assert new_product.price == 180000.0


def test_price_no_valid(product2, capsys):
    product2.price = -100
    captured = capsys.readouterr()
    assert captured.out == """Цена не должна быть "0" или отрицательная\n"""


def test_price_valid(product2):
    product2.price = 180000.0
    assert product2.price == 180000.0


def test_str_magics(product2, capsys):
    print(product2)
    captured = capsys.readouterr()
    assert captured.out == """Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n\n"""


def test_add(product1, product2):
    assert product1 + product2 == 1334000


def test_call(product2, capsys):
    print(product2())
    captured = capsys.readouterr()
    assert captured.out == """Xiaomi Redmi Note 11, харрактеристики: 1024GB, Синий, 31000.0 руб. Остаток: 14 шт.\n\n"""
