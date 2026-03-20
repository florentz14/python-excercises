from tabulate import tabulate

class Invoice:
    # contructor method
    def __init__(self, invoice_id: str, customer_name: str, amount: float, quantity: int = 0) -> None:
        # run validations to the received arguments
        assert amount >= 0, f"Amount {amount} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"
        
        # assign to selft object attributes
        self.invoice_id: str = invoice_id
        self.customer_name: str = customer_name
        self.amount: float = amount
        self.quantity: int = quantity
        self.is_paid: bool = False
    
    # mark as paid
    def mark_as_paid(self) -> None:
        self.is_paid = True

    # check if overdue
    def is_overdue(self, days_overdue: int) -> bool:
        return days_overdue > 30

    # calculate total price
    def calculate_total_price(self) -> float:
        return self.amount * self.quantity    

    # get invoice info
    def get_invoice_info(self) -> str:
        return f"Invoice {self.invoice_id} for {self.customer_name}: ${self.amount:.2f} - {'Paid' if self.is_paid else 'Unpaid'}"
    
    # convert invoice to table row
    def to_row(self) -> list:
        """Convert invoice to table row format."""
        return [
            self.invoice_id,
            self.customer_name,
            self.amount,
            self.quantity,
            self.calculate_total_price(),
            "Paid" if self.is_paid else "Unpaid"
        ]

# display invoices table
def display_invoices_table(invoices: list, title: str) -> None:
    """Display invoices in a formatted table."""
    print(f"\n{title}")
    
    # define table headers
    headers = ["Invoice ID", "Customer", "Unit Price", "Quantity", "Total", "Status"]
    
    # convert invoices to table rows
    data = [invoice.to_row() for invoice in invoices]
    
    # display table with fancy format and proper formatting
    print(tabulate(data, headers, tablefmt="fancy_grid", 
                   floatfmt=".2f", colalign=("left", "left", "right", "right", "right", "center")))

# display summary table
def display_summary_table(invoices: list) -> None:
    """Display summary information in table format."""
    print("\n=== Invoice Summary ===")
    
    # collect summary data
    summary_data = []

    # iterate over invoices with index
    for i, invoice in enumerate(invoices, 1):
        summary_data.append([
            f"Invoice {i}",
            invoice.calculate_total_price(),
            "Yes" if invoice.is_overdue(35) else "No" if i == 2 else "Yes"
        ])
    
    # define table headers
    headers = ["Invoice", "Total Price", "Overdue (35 days)"]
    
    # display table with mixed format and proper formatting
    print(tabulate(summary_data, headers, tablefmt="mixed_grid", 
                   floatfmt=".2f", colalign=("left", "right", "center")))

# main function
def main() -> None:
    print("=== Invoice System ===")
    
    # create invoices
    invoice1 = Invoice("INV-001", "John Doe", 150.00, 7)
    invoice2 = Invoice("INV-002", "Jane Smith", 200.00, 5)
    invoice3 = Invoice("INV-003", "Bob Johnson", 100.00)
    
    invoices = [invoice1, invoice2, invoice3]
    
    # display initial invoices
    display_invoices_table(invoices, "Initial Invoices:")
    
    # mark invoice1 as paid and update
    invoice1.mark_as_paid()
    display_invoices_table(invoices, "Updated Invoices (Invoice 1 Marked as Paid):")
    
    # display summary table
    display_summary_table(invoices)

if __name__ == "__main__":
    main()
