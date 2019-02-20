# -*- coding: utf-8 -*-



class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.name != "Sulfuras, Hand of Ragnaros":
                    self.__update_item(item, 'dec')
                    if "Conjured" in item.name:
                        self.__update_item(item, 'dec')
            else:
                self.__update_item(item, 'inc')
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        self.__update_item(item, 'inc')
                    if item.sell_in < 6:
                        self.__update_item(item, 'inc')
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            self.__update_item(item, 'dec')
                            if "Conjured" in item.name:
                                self.__update_item(item, 'dec')
                    else:
                        item.quality = item.quality - item.quality
                else:
                    self.__update_item(item, 'inc')

    def __update_item(self, item, direction):
        if item.quality < 50 and direction == 'inc':
            item.quality += 1
        if item.quality > 0 and direction == 'dec':
            item.quality -= 1
        return item.quality

