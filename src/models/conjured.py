from src.models.item import Item


class Conjured(Item):
    def update_item(self):
        if self.sell_in > 0:
            self.quality -= 2
        elif self.sell_in <= 0:
            self.quality -= 4
        self.sell_in -= 1
