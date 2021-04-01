from app import InvoiceItem, Invoice

if __name__ == '__main__':
    milk = InvoiceItem('milk', 1, 1.23)
    chocolate = InvoiceItem('chocolate', 1, 3.45)
    eggs = InvoiceItem('eggs', 3, 3.00)

    invoice_items = [milk, chocolate, eggs]

    invoice = Invoice(
        items=invoice_items,
        tax=0.13,
        discount=0.0
    )

    print(f"invoice total: {invoice.total()}")

