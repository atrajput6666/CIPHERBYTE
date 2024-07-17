from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_receipt(transaction_id, date, items, total, customer_name, receipt_file):
    c = canvas.Canvas(receipt_file, pagesize=letter)
    width, height = letter

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1 * inch, height - 1 * inch, "Payment Receipt")

    # Transaction Info
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1.5 * inch, f"Transaction ID: {transaction_id}")
    c.drawString(1 * inch, height - 1.75 * inch, f"Date: {date}")
    c.drawString(1 * inch, height - 2 * inch, f"Customer Name: {customer_name}")

    # Items
    c.drawString(1 * inch, height - 2.5 * inch, "Items:")
    y = height - 3 * inch
    for item, price in items.items():
        c.drawString(1.5 * inch, y, f"{item}: ${price:.2f}")
        y -= 0.25 * inch

    # Total
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1 * inch, y - 0.25 * inch, f"Total: ${total:.2f}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(1 * inch, 1 * inch, "Thank you for your business!")

    c.save()

if __name__ == "__main__":
    transaction_id = "123456789"
    date = "2024-07-13"
    customer_name = "Ankit tomar"
    items = {
        "Item 1": 19.99,
        "Item 2": 29.99,
        "Item 3": 9.99
    }
    total = sum(items.values())
    receipt_file = "receipt.pdf"

    create_receipt(transaction_id, date, items, total, customer_name, receipt_file)
    print(f"Receipt saved as {receipt_file}")
