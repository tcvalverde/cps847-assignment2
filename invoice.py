from typing import List
from functools import reduce
from invoice_item import InvoiceItem


class Invoice:
    def __init__(self, items: List[InvoiceItem], tax: float = 0.13, discount: float = 0):
        self.items = items
        self.tax = tax
        self.discount = discount

    def total(self) -> float:
        items_total = reduce(lambda total, item: total + item.total(), self.items, 0.0)
        items_total_discounted = items_total * (1.0 - self.discount)
        return round(items_total_discounted * (1.0 - self.tax), 2)
