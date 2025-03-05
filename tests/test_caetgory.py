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


def test_add_product(category1, product3):
    category1.add_product(product3)
    assert category1.products == """55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"""


def test_add_product_no_valid(category1, capsys):
    category1.add_product(1)
    captured = capsys.readouterr()
    assert captured.out == "Объект 1 не является экземпляром класса Product\n\n"
