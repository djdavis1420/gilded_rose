from src.gilded_rose import GildedRose
from src.models.item import Item


def test_update_quality__sell_in_lower_by_one():
    ashbringer = Item('Ashbringer', 25, 40)
    warglaives = Item('Warglaives', 35, 40)
    gilded_rose = GildedRose([ashbringer, warglaives])

    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in == 24
    assert ashbringer.sell_in == 24
    assert warglaives.sell_in == 34


def test_update_quality__quality_lower_by_one():
    ashbringer = Item('Ashbringer', 25, 40)
    warglaives = Item('Warglaives', 35, 40)
    gilded_rose = GildedRose([ashbringer, warglaives])

    gilded_rose.update_quality()

    assert ashbringer.quality == 39
    assert warglaives.quality == 39


def test_update_quality__quality_lower_by_2x_after_sell_in():
    ashbringer = Item('Ashbringer', -1, 40)
    gilded_rose = GildedRose([ashbringer])

    gilded_rose.update_quality()

    assert ashbringer.quality == 38


def test_update_quality__quality_not_less_than_0():
    ashbringer = Item('Ashbringer', 10, 0)
    negatives = [-5, -4, -3, -2, -1]
    gilded_rose = GildedRose([ashbringer])

    gilded_rose.update_quality()

    assert ashbringer.quality != -1
    assert ashbringer.quality not in negatives


def test_update_quality__AB_quality_plus_1():
    aged_brie = Item('Aged Brie', 3, 10)
    gilded_rose = GildedRose([aged_brie])

    gilded_rose.update_quality()

    assert aged_brie.quality == 11


def test_update_quality__AB_quality_plus_2_after_sell_in():
    aged_brie = Item('Aged Brie', 0, 10)
    gilded_rose = GildedRose([aged_brie])

    gilded_rose.update_quality()

    assert aged_brie.quality == 12


def test_update_quality__quality_not_more_than_50():
    ashbringer = Item('Ashbringer', 10, 50)
    aged_brie = Item('Aged Brie', 10, 50)
    backstage_passes = Item('Backstage passes to a TAFKAL80ETC concert', 3, 50)
    fifties = [51, 52, 53, 54, 55]
    gilded_rose = GildedRose([ashbringer, aged_brie, backstage_passes])

    gilded_rose.update_quality()

    assert ashbringer.quality == 49
    assert aged_brie.quality != 51
    assert aged_brie.quality not in fifties
    assert backstage_passes.quality != 53
    assert backstage_passes.quality not in fifties


def test_update_quality__sulfuras_never_changes():
    sulfuras = Item('Sulfuras, Hand of Ragnaros', 10, 80)
    gilded_rose = GildedRose([sulfuras])

    gilded_rose.update_quality()

    assert sulfuras.quality == 80
    assert sulfuras.sell_in == 10


def test_update_quality__BSP_quality_plus_3_if_sell_in_less_than_5():
    backstage_passes1 = Item('Backstage passes to a TAFKAL80ETC concert', 3, 10)
    backstage_passes2 = Item('Backstage passes to a TAFKAL80ETC concert', 3, 49)
    gilded_rose = GildedRose([backstage_passes1, backstage_passes2])

    gilded_rose.update_quality()

    assert backstage_passes1.quality == 13
    assert backstage_passes2.quality == 50


def test_update_quality__BSP_quality_plus_2_if_sell_in_less_than_10_and_more_than_5():
    backstage_passes1 = Item('Backstage passes to a TAFKAL80ETC concert', 8, 10)
    backstage_passes2 = Item('Backstage passes to a TAFKAL80ETC concert', 8, 49)

    gilded_rose = GildedRose([backstage_passes1, backstage_passes2])

    gilded_rose.update_quality()

    assert backstage_passes1.quality == 12
    assert backstage_passes2.quality == 50


def test_update_quality__BSP_quality_plus_1_if_sell_in_more_than_10():
    backstage_passes1 = Item('Backstage passes to a TAFKAL80ETC concert', 13, 10)
    backstage_passes2 = Item('Backstage passes to a TAFKAL80ETC concert', 13, 49)
    backstage_passes3 = Item('Backstage passes to a TAFKAL80ETC concert', 13, 50)
    gilded_rose = GildedRose([backstage_passes1, backstage_passes2, backstage_passes3])

    gilded_rose.update_quality()

    assert backstage_passes1.quality == 11
    assert backstage_passes2.quality == 50
    assert backstage_passes3.quality == 50


def test_update_quality__BSP_quality_to_0_if_sell_in_is_0():
    backstage_passes = Item('Backstage passes to a TAFKAL80ETC concert', 0, 10)
    gilded_rose = GildedRose([backstage_passes])

    gilded_rose.update_quality()

    assert backstage_passes.quality == 0


def test_update_quality__conjured_lower_by_two():
    conjured_bread = Item('Conjured Bread', 10, 20)
    conjured_water = Item('Conjured Water', 3, 5)
    gilded_rose = GildedRose([conjured_bread, conjured_water])

    gilded_rose.update_quality()

    assert conjured_bread.quality == 18
    assert conjured_water.quality == 3


def test_update_quality__conjured_lower_by_2x_after_sell_in():
    conjured_bread = Item('Conjured Bread', 0, 20)
    conjured_water = Item('Conjured Water', 0, 6)
    gilded_rose = GildedRose([conjured_bread, conjured_water])

    gilded_rose.update_quality()

    assert conjured_bread.quality == 16
    assert conjured_water.quality == 2

