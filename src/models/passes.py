from src.models.item import Item


class Passes(Item):
    def update_item(self):
        self.__update_item()
        if self.sell_in < 11:
            self.__update_item()
        if self.sell_in < 6:
            self.__update_item()
        if self.sell_in <= 0:
            self.quality = 0

    def __update_item(self, amount=1):
        while self.quality < 50 and amount >= 1:
            self.quality += 1
            amount -= 1
        return self.quality
