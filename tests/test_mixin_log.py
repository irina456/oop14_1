from src.product import LawnGrass, Smartphone


def test_LawnGrass(capsys):
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    captured = capsys.readouterr()
    assert (
        captured.out
        == """  Был создан экземпляр класса LawnGrass
        Входные данные:
            Наименование: Газонная трава
            Описание: Элитная трава для газона
            Цена: 500.0
            Колличество: 20\n"""
    )


def test_Smartphone(capsys):
    Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    captured = capsys.readouterr()
    assert (
        captured.out
        == """  Был создан экземпляр класса Smartphone
        Входные данные:
            Наименование: Xiaomi Redmi Note 11
            Описание: 1024GB, Синий
            Цена: 31000.0
            Колличество: 14\n"""
    )
