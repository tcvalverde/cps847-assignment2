import unittest

from invoice import Invoice
from invoice_item import InvoiceItem


class TestInvoice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = [
            InvoiceItem('milk', 1, 1.0),
            InvoiceItem('chocolate', 1, 3.0),
            InvoiceItem('eggs', 3, 3.00)
        ]

    def test_invoice_total_success_1(self):
        invoice = Invoice(self.items)
        expected_total = 11.31
        self.assertEqual(invoice.total(), expected_total)

    def test_invoice_total_success_2(self):
        tax = 0.15  # 15%
        invoice = Invoice(items=self.items, tax=tax)
        expected_total = 11.05

        self.assertEqual(invoice.total(), expected_total)

    def test_invoice_total_success_3(self):
        discount = 0.15  # 15%
        invoice = Invoice(items=self.items, discount=discount)
        expected_total = 9.61

        self.assertEqual(invoice.total(), expected_total)



