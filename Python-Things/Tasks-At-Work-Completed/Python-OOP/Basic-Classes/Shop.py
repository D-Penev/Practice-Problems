class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items
    def get_items_count(self):
        return len(self.items)

shop = Shop('Test', ['bai ivan golemiq', 'bai_ivan_malkiq', 'bai_ivan_zavryshtaneto'])
print(shop.get_items_count())