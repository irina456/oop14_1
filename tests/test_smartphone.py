import pytest


def test_class_smartphone(smartphone1):
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_add_smartphone(smartphone1, smartphone2):
    smartphone_sum = smartphone1 + smartphone2
    assert smartphone_sum == 1334000


def test_smartphone_no_valid(smartphone1, grass1):
    with pytest.raises(TypeError):
        assert smartphone1 + grass1 == "Объект 1 не является экземпляром класса Product"