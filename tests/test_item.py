"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item = Item("Shirt", 20.0, 5)
    assert item.calculate_total_price() == 100.0


def test_apply_discount():
    item = Item("Shirt", 20.0, 5)
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 18.0


def test_add_to_all():
    item1 = Item("Shirt", 20.0, 5)
    item2 = Item("Pants", 30.0, 3)
    Item.all.append(item1)
    Item.all.append(item2)
    assert len(Item.all) == 2
    assert Item.all[0].name == "Shirt"
    assert Item.all[1].name == "Pants"
