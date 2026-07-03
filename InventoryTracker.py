class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def checkStockLevel(self, item):
        return self.inventory.get(item, 0)

    def alertLowStock(self, item, threshold=5):
        if self.checkStockLevel(item) < threshold:
            print(f"Alert: {item} is low on stock!")
