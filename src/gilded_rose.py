# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            elif item.name == "Aged Brie":
                self.__update_item(item, 'inc')
                if item.sell_in <= 0:
                    self.__update_item(item, 'inc')

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.__update_item(item, 'inc')
                if item.sell_in < 11:
                    self.__update_item(item, 'inc')
                if item.sell_in < 6:
                    self.__update_item(item, 'inc')
                if item.sell_in <= 0:
                    item.quality = 0

            elif "Conjured" in item.name:
                if item.sell_in > 0:
                    self.__update_item(item, 'dec', 2)
                elif item.sell_in <= 0:
                    self.__update_item(item, 'dec', 4)

            else:
                if item.sell_in <= 0:
                    self.__update_item(item, 'dec', 2)
                elif item.quality > 0:
                    self.__update_item(item, 'dec')

            item.sell_in -= 1

    def __update_item(self, item, direction, amount=1):
        while item.quality < 50 and direction == 'inc' and amount >= 1:
            item.quality += 1
            amount -= 1
        while item.quality > 0 and direction == 'dec' and amount >= 1:
            item.quality -= 1
            amount -= 1
        return item.quality
