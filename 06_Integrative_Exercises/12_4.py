# Exercise 4: Table with Headings
# Add column headings to a table containing item names, prices, and quantities.
# Format prices with currency symbols and decimal precision.

print("Exercise 4: Table with Headings")
print("-" * 40)

# Print headings
print(f"{'Item':<12}{'Price':<8}{'Quantity':<8}")
print("-" * 28)

# Row 1
item1 = "Pencil"
price1 = 0.50
qty1 = 20
print(f"{item1:<12}${price1:<7.2f}{qty1:<8}")

# Row 2
item2 = "Notebook"
price2 = 1.75
qty2 = 5
print(f"{item2:<12}${price2:<7.2f}{qty2:<8}")

# Row 3
item3 = "Eraser"
price3 = 0.25
qty3 = 50
print(f"{item3:<12}${price3:<7.2f}{qty3:<8}")

print("\nNote: The format '.2f' formats prices to 2 decimal places")
