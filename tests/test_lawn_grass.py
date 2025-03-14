import pytest


def test_class_lawn_grass(grass1):
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_add_grass(grass1, grass2):
    grass_sum = grass1 + grass2
    assert grass_sum == 16750


def test_grass_no_valid(smartphone2, grass2):
    with pytest.raises(TypeError):
        assert smartphone2 + grass2 == "Объект 1 не является экземпляром класса Product"
