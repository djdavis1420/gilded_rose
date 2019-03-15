from src.models.item import Item


class AgedBrie(Item):
    def update_item(self):
        if self.sell_in <= 0 and self.quality <= 48:
            self.quality += 2
        elif self.sell_in > 0 and self.quality < 50:
            self.quality += 1
        self.sell_in -= 1
