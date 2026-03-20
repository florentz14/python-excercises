# -------------------------------------------------
# File Name: 59_invoice_detail.py
# Author: Florentino
# Date: 3/18/26
# Description: InvoiceDetail class for line items and enhanced Invoice system.
# -------------------------------------------------

from tabulate import tabulate

class InvoiceDetail:
    """Represents a single line item in an invoice."""
    
    def __init__(self, product_name: str, quantity: int, unit_price: float) -> None:
        # run validations to the received arguments
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"
        assert unit_price >= 0, f"Unit price {unit_price} cannot be negative"
        
        # assign to self object attributes
        self.product_name: str = product_name
        self.quantity: int = quantity
        self.unit_price: float = unit_price
    
    # calculate line total
    def calculate_line_total(self) -> float:
        """Calculate total price for this line item."""
        return self.quantity * self.unit_price
    
    #apply discount
    def apply_discount(self, discount: float) -> None:
        """Apply a discount to the unit price."""
        self.unit_price *= (1 - discount)

    # get line info
    def get_line_info(self) -> str:
        """Get formatted line item information."""
        return f"{self.product_name}: {self.quantity} x ${self.unit_price:.2f} = ${self.calculate_line_total():.2f}"
    
    # convert to table row
    def to_row(self) -> list:
        """Convert invoice detail to table row format."""
        return [
            self.product_name,
            self.quantity,
            f"${self.unit_price:.2f}",
            f"${self.calculate_line_total():.2f}"
        ]

class Invoice:
    """Enhanced invoice class with multiple line items."""
    
    def __init__(self, invoice_id: str, customer_name: str) -> None:
        self.invoice_id: str = invoice_id
        self.customer_name: str = customer_name
        self.details: list[InvoiceDetail] = []
        self.is_paid: bool = False
    
    # add line item
    def add_detail(self, product_name: str, quantity: int, unit_price: float) -> None:
        """Add a line item to the invoice."""
        detail = InvoiceDetail(product_name, quantity, unit_price)
        self.details.append(detail)
    
    # remove line item
    def remove_detail(self, index: int) -> bool:
        """Remove a line item by index."""
        if 0 <= index < len(self.details):
            del self.details[index]
            return True
        return False
    
    # mark as paid
    def mark_as_paid(self) -> None:
        self.is_paid = True
    
    # check if overdue
    def is_overdue(self, days_overdue: int) -> bool:
        return days_overdue > 30
    
    # calculate total price
    def calculate_total_price(self) -> float:
        """Calculate total price for all line items."""
        return sum(detail.calculate_line_total() for detail in self.details)
    
    # get invoice info
    def get_invoice_info(self) -> str:
        total = self.calculate_total_price()
        status = "Paid" if self.is_paid else "Unpaid"
        return f"Invoice {self.invoice_id} for {self.customer_name}: ${total:.2f} - {status}"
    
    # convert to table row
    def to_row(self) -> list:
        """Convert invoice to table row format."""
        return [
            self.invoice_id,
            self.customer_name,
            len(self.details),
            f"${self.calculate_total_price():.2f}",
            "Paid" if self.is_paid else "Unpaid"
        ]

def display_invoice_details_table(invoice: Invoice) -> None:
    """Display detailed line items for a single invoice."""
    print(f"\n=== Invoice Details: {invoice.invoice_id} ===")
    print(f"Customer: {invoice.customer_name}")
    print(f"Status: {'Paid' if invoice.is_paid else 'Unpaid'}")
    
    if not invoice.details:
        print("No line items found.")
        return
    
    headers = ["Product", "Quantity", "Unit Price", "Line Total"]
    
    # Convert details to table rows
    data = [detail.to_row() for detail in invoice.details]
    
    # Display table
    print(tabulate(data, headers, tablefmt="fancy_grid", 
                   colalign=("left", "right", "right", "right")))
    
    # Display total
    print(f"\nInvoice Total: ${invoice.calculate_total_price():.2f}")

def display_invoices_summary_table(invoices: list[Invoice], title: str) -> None:
    """Display summary of multiple invoices."""
    print(f"\n{title}")
    
    if not invoices:
        print("No invoices found.")
        return
    
    headers = ["Invoice ID", "Customer", "Items", "Total", "Status"]
    
    # Convert invoices to table rows
    data = [invoice.to_row() for invoice in invoices]
    
    # Display table
    print(tabulate(data, headers, tablefmt="mixed_grid", 
                   colalign=("left", "left", "right", "right", "center")))

def main() -> None:
    print("=== Enhanced Invoice System with InvoiceDetail ===")
    
    # Create invoices
    invoice1 = Invoice("INV-001", "John Doe")
    invoice2 = Invoice("INV-002", "Jane Smith")
    invoice3 = Invoice("INV-003", "Bob Johnson")
    
    # Add line items to invoice1
    invoice1.add_detail("Laptop", 1, 999.99)
    invoice1.add_detail("Mouse", 2, 25.50)
    invoice1.add_detail("Keyboard", 1, 75.00)
    
    # Add line items to invoice2
    invoice2.add_detail("Monitor", 2, 299.99)
    invoice2.add_detail("USB Cable", 5, 10.00)
    
    # Add line items to invoice3
    invoice3.add_detail("Webcam", 1, 89.99)
    invoice3.add_detail("Headphones", 1, 149.99)
    
    invoices = [invoice1, invoice2, invoice3]
    
    # Display summary table
    display_invoices_summary_table(invoices, "All Invoices Summary:")
    
    # Display detailed view of first invoice
    display_invoice_details_table(invoice1)
    
    # Mark invoice1 as paid and update
    invoice1.mark_as_paid()
    display_invoices_summary_table(invoices, "Updated Summary (Invoice 1 Paid):")
    
    # Display all invoice details
    for invoice in invoices:
        display_invoice_details_table(invoice)

if __name__ == "__main__":
    main()
