class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_item(self):
        if self.sell_in <= 0:
            self.quality -= 2
        elif self.quality > 0:
            self.quality -= 1
        self.sell_in -= 1
