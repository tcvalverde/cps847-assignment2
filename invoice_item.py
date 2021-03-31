class InvoiceItem:
    def __init__(self, name: str, unit: int, price: float):
        self.name = name
        self.unit = unit
        self.price = price

    def total(self):
        return self.price * self.unit
