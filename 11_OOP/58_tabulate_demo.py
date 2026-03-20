# -------------------------------------------------
# File Name: 58_tabulate_demo.py
# Author: Florentino
# Date: 3/18/26
# Description: Demo of tabulate library for pretty printing tables.
# -------------------------------------------------

from tabulate import tabulate

def basic_table_example():
    """Basic table example with headers."""
    print("=== Basic Table Example ===")
    
    data = [
        ["John Doe", 25, "Engineer"],
        ["Jane Smith", 30, "Designer"],
        ["Bob Johnson", 35, "Manager"]
    ]
    
    headers = ["Name", "Age", "Position"]
    
    print(tabulate(data, headers, tablefmt="grid"))
    print()

def invoice_table_example():
    """Invoice data table example."""
    print("=== Invoice Table Example ===")
    
    invoices = [
        ["INV-001", "John Doe", 150.00, "Unpaid"],
        ["INV-002", "Jane Smith", 200.00, "Unpaid"],
        ["INV-003", "Bob Johnson", 100.00, "Paid"]
    ]
    
    headers = ["Invoice ID", "Customer", "Amount", "Status"]
    
    print(tabulate(invoices, headers, tablefmt="fancy_grid", floatfmt=".2f"))
    print()

def different_formats_example():
    """Show different table formats."""
    print("=== Different Table Formats ===")
    
    data = [
        ["Product A", 10, 25.50],
        ["Product B", 15, 30.75],
        ["Product C", 8, 15.25]
    ]
    headers = ["Product", "Quantity", "Price"]
    
    formats = ["grid", "fancy_grid", "pipe", "simple", "plain", "html"]
    
    for fmt in formats:
        print(f"Format: {fmt}")
        print(tabulate(data, headers, tablefmt=fmt, floatfmt=".2f"))
        print()

def student_grades_example():
    """Student grades table with calculations."""
    print("=== Student Grades Table ===")
    
    students = [
        ["Alice", 85, 92, 88, 265, 88.33],
        ["Bob", 78, 85, 90, 253, 84.33],
        ["Charlie", 92, 88, 95, 275, 91.67],
        ["Diana", 88, 90, 85, 263, 87.67]
    ]
    
    headers = ["Name", "Test 1", "Test 2", "Test 3", "Total", "Average"]
    
    print(tabulate(students, headers, tablefmt="mixed_grid", floatfmt=".2f"))
    print()

def database_style_table():
    """Database-style table with alignment."""
    print("=== Database Style Table ===")
    
    products = [
        ["P001", "Laptop", 999.99, 15],
        ["P002", "Mouse", 25.50, 100],
        ["P003", "Keyboard", 75.00, 50],
        ["P004", "Monitor", 299.99, 25]
    ]
    
    headers = ["ID", "Product", "Price", "Stock"]
    
    # Custom alignment: left, left, right, right
    colalign = ("left", "left", "right", "right")
    
    print(tabulate(products, headers, tablefmt="double_grid", 
                  floatfmt=".2f", colalign=colalign))
    print()

def main():
    """Main function to demonstrate all examples."""
    print("Tabulate Library Demo")
    print("=" * 50)
    print()
    
    basic_table_example()
    invoice_table_example()
    different_formats_example()
    student_grades_example()
    database_style_table()
    
    print("=== Installation ===")
    print("To install tabulate: pip install tabulate")
    print()
    print("=== Common Table Formats ===")
    formats_info = [
        ["grid", "Grid with borders"],
        ["fancy_grid", "Fancy grid with double borders"],
        ["pipe", "Pipe format (like Markdown)"],
        ["simple", "Simple format"],
        ["plain", "Plain text"],
        ["html", "HTML table"],
        ["latex", "LaTeX table"],
        ["mixed_grid", "Mixed grid format"]
    ]
    print(tabulate(formats_info, ["Format", "Description"], tablefmt="simple"))

if __name__ == "__main__":
    main()
