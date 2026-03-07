# -------------------------------------------------
# File: 25_inventory.py
# Description: Inventory system - practical application.
#              Composition, encapsulation, data management.
# -------------------------------------------------

from typing import List, Dict, Optional
from datetime import datetime, date
import json


class Product:
    """Product class for inventory items."""

    def __init__(self, product_id: str, name: str, price: float,
                 category: str, description: str = ""):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._category = category
        self._description = description

    @property
    def product_id(self) -> str:
        """Get product ID (read-only)."""
        return self._product_id

    @property
    def name(self) -> str:
        """Get product name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Set product name with validation."""
        if not value or not value.strip():
            raise ValueError("Product name cannot be empty")
        self._name = value.strip()

    @property
    def price(self) -> float:
        """Get product price."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Set product price with validation."""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number")
        self._price = float(value)

    @property
    def category(self) -> str:
        """Get product category."""
        return self._category

    @category.setter
    def category(self, value: str):
        """Set product category with validation."""
        if not value or not value.strip():
            raise ValueError("Category cannot be empty")
        self._category = value.strip().title()

    @property
    def description(self) -> str:
        """Get product description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set product description."""
        self._description = value.strip()

    def get_info(self) -> str:
        """Get product information."""
        info = f"ID: {self._product_id}\n"
        info += f"Name: {self._name}\n"
        info += f"Price: ${self._price:.2f}\n"
        info += f"Category: {self._category}"
        if self._description:
            info += f"\nDescription: {self._description}"
        return info

    def __str__(self) -> str:
        """String representation."""
        return f"{self._name} (${self._price:.2f})"

    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Product(id='{self._product_id}', name='{self._name}', price={self._price})"

    def __eq__(self, other) -> bool:
        """Check equality by product ID."""
        if not isinstance(other, Product):
            return False
        return self._product_id == other._product_id

    def __hash__(self) -> int:
        """Hash based on product ID."""
        return hash(self._product_id)


class InventoryItem:
    """Inventory item combining product with quantity and location."""

    def __init__(self, product: Product, quantity: int, location: str):
        self.product = product
        self.quantity = quantity
        self.location = location
        self.last_updated = datetime.now()

    @property
    def quantity(self) -> int:
        """Get quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        """Set quantity with validation."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self._quantity = value
        self.last_updated = datetime.now()

    @property
    def location(self) -> str:
        """Get location."""
        return self._location

    @location.setter
    def location(self, value: str):
        """Set location with validation."""
        if not value or not value.strip():
            raise ValueError("Location cannot be empty")
        self._location = value.strip().upper()

    @property
    def total_value(self) -> float:
        """Calculate total value of inventory item."""
        return self._quantity * self.product.price

    def add_stock(self, amount: int):
        """Add stock to inventory."""
        if amount <= 0:
            raise ValueError("Amount to add must be positive")
        self.quantity += amount

    def remove_stock(self, amount: int):
        """Remove stock from inventory."""
        if amount <= 0:
            raise ValueError("Amount to remove must be positive")
        if amount > self._quantity:
            raise ValueError(
                f"Insufficient stock. Available: {self._quantity}")
        self.quantity -= amount

    def is_low_stock(self, threshold: int = 10) -> bool:
        """Check if stock is below threshold."""
        return self._quantity <= threshold

    def get_info(self) -> str:
        """Get inventory item information."""
        info = f"Product: {self.product.name}\n"
        info += f"Quantity: {self._quantity}\n"
        info += f"Location: {self._location}\n"
        info += f"Total Value: ${self.total_value:.2f}\n"
        info += f"Last Updated: {self.last_updated.strftime('%Y-%m-%d %H:%M')}"
        return info

    def __str__(self) -> str:
        """String representation."""
        return f"{self.product.name} (Qty: {self._quantity}, Loc: {self._location})"


class Inventory:
    """Inventory management system."""

    def __init__(self):
        # product_id -> InventoryItem
        self._items: Dict[str, InventoryItem] = {}

    def add_product(self, product: Product, quantity: int, location: str):
        """Add a product to inventory."""
        if product.product_id in self._items:
            raise ValueError(
                f"Product {product.product_id} already exists in inventory")

        item = InventoryItem(product, quantity, location)
        self._items[product.product_id] = item
        return f"Added {product.name} to inventory"

    def update_quantity(self, product_id: str, quantity: int):
        """Update quantity of a product."""
        if product_id not in self._items:
            raise ValueError(f"Product {product_id} not found in inventory")

        self._items[product_id].quantity = quantity
        return f"Updated {self._items[product_id].product.name} quantity to {quantity}"

    def remove_product(self, product_id: str):
        """Remove a product from inventory."""
        if product_id not in self._items:
            raise ValueError(f"Product {product_id} not found in inventory")

        product_name = self._items[product_id].product.name
        del self._items[product_id]
        return f"Removed {product_name} from inventory"

    def get_item(self, product_id: str) -> Optional[InventoryItem]:
        """Get inventory item by product ID."""
        return self._items.get(product_id)

    def get_all_items(self) -> List[InventoryItem]:
        """Get all inventory items."""
        return list(self._items.values())

    def get_items_by_category(self, category: str) -> List[InventoryItem]:
        """Get items by category."""
        return [item for item in self._items.values()
                if item.product.category.lower() == category.lower()]

    def get_items_by_location(self, location: str) -> List[InventoryItem]:
        """Get items by location."""
        return [item for item in self._items.values()
                if item.location == location.upper()]

    def get_low_stock_items(self, threshold: int = 10) -> List[InventoryItem]:
        """Get items with low stock."""
        return [item for item in self._items.values() if item.is_low_stock(threshold)]

    def get_total_value(self) -> float:
        """Calculate total value of all inventory."""
        return sum(item.total_value for item in self._items.values())

    def get_inventory_summary(self) -> str:
        """Get inventory summary."""
        total_items = len(self._items)
        total_value = self.get_total_value()
        low_stock = len(self.get_low_stock_items())

        summary = f"Inventory Summary\n"
        summary += f"Total Products: {total_items}\n"
        summary += f"Total Value: ${total_value:.2f}\n"
        summary += f"Low Stock Items: {low_stock}"

        if total_items > 0:
            avg_value = total_value / total_items
            summary += f"\nAverage Product Value: ${avg_value:.2f}"

        return summary

    def search_products(self, query: str) -> List[InventoryItem]:
        """Search products by name or ID."""
        query = query.lower()
        results = []
        for item in self._items.values():
            if (query in item.product.product_id.lower() or
                query in item.product.name.lower() or
                    query in item.product.category.lower()):
                results.append(item)
        return results

    def transfer_stock(self, product_id: str, from_location: str, to_location: str, quantity: int):
        """Transfer stock between locations."""
        item = self.get_item(product_id)
        if not item:
            raise ValueError(f"Product {product_id} not found")

        if item.location != from_location.upper():
            raise ValueError(f"Product is not at location {from_location}")

        if quantity > item.quantity:
            raise ValueError(
                f"Insufficient stock at {from_location}. Available: {item.quantity}")

        # Create new item at destination or update existing
        dest_item = None
        for existing_item in self._items.values():
            if (existing_item.product.product_id == product_id and
                    existing_item.location == to_location.upper()):
                dest_item = existing_item
                break

        if dest_item:
            dest_item.add_stock(quantity)
        else:
            new_item = InventoryItem(item.product, quantity, to_location)
            self._items[f"{product_id}_{to_location.upper()}"] = new_item

        item.remove_stock(quantity)
        return f"Transferred {quantity} units of {item.product.name} from {from_location} to {to_location}"

    def export_to_json(self, filename: str):
        """Export inventory to JSON file."""
        data = {
            "export_date": datetime.now().isoformat(),
            "total_items": len(self._items),
            "total_value": self.get_total_value(),
            "items": []
        }

        for item in self._items.values():
            item_data = {
                "product_id": item.product.product_id,
                "name": item.product.name,
                "price": item.product.price,
                "category": item.product.category,
                "description": item.product.description,
                "quantity": item.quantity,
                "location": item.location,
                "total_value": item.total_value,
                "last_updated": item.last_updated.isoformat()
            }
            data["items"].append(item_data)

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

        return f"Inventory exported to {filename}"


# Demonstration
if __name__ == "__main__":
    print("=== Inventory System Demo ===\n")

    # Create inventory
    inventory = Inventory()

    # Create products
    products = [
        Product("P001", "Laptop", 999.99, "Electronics",
                "High-performance laptop"),
        Product("P002", "Mouse", 25.50, "Electronics",
                "Wireless optical mouse"),
        Product("P003", "Book", 15.99, "Books", "Python programming guide"),
        Product("P004", "Chair", 149.99, "Furniture",
                "Ergonomic office chair"),
        Product("P005", "Pen", 2.99, "Office Supplies", "Blue ballpoint pen")
    ]

    # Add products to inventory
    print("Adding products to inventory:")
    for product in products:
        result = inventory.add_product(product, 50, "WAREHOUSE_A")
        print(f"  {result}")

    # Update some quantities
    print(f"\n{inventory.update_quantity('P001', 75)}")
    print(f"{inventory.update_quantity('P002', 5)}")  # Low stock

    # Get inventory summary
    print(f"\n{inventory.get_inventory_summary()}")

    # Search products
    print(f"\nSearching for 'book':")
    search_results = inventory.search_products("book")
    for item in search_results:
        print(f"  {item}")

    # Get low stock items
    print(f"\nLow stock items (threshold: 10):")
    low_stock = inventory.get_low_stock_items(10)
    for item in low_stock:
        print(f"  {item}")

    # Transfer stock
    print(f"\n{inventory.transfer_stock('P001', 'WAREHOUSE_A', 'STORE_B', 25)}")

    # Get items by category
    print(f"\nElectronics items:")
    electronics = inventory.get_items_by_category("Electronics")
    for item in electronics:
        print(f"  {item.get_info()}")
        print()

    # Export to JSON
    print(inventory.export_to_json("inventory_export.json"))

    print("\n=== OOP Concepts Demonstrated ===")
    print("- Composition: Inventory contains InventoryItem, which contains Product")
    print("- Encapsulation: Private attributes with property accessors")
    print("- Data validation: Input validation throughout")
    print("- Class relationships: Product -> InventoryItem -> Inventory")
    print("- Method delegation: Inventory delegates to InventoryItem")
    print("- Data persistence: JSON export functionality")
    print("- Search and filtering: Multiple query methods")

    print("\n=== Error Handling Demo ===")
    try:
        # Duplicate product
        inventory.add_product(products[0], 10, "WAREHOUSE_A")
    except ValueError as e:
        print(f"Duplicate product error: {e}")

    try:
        inventory.update_quantity("P999", 100)  # Non-existent product
    except ValueError as e:
        print(f"Product not found error: {e}")

    try:
        item = inventory.get_item("P002")
        if item:
            item.remove_stock(100)  # Insufficient stock
    except ValueError as e:
        print(f"Insufficient stock error: {e}")

    try:
        invalid_product = Product("P006", "", -10, "")  # Invalid product
    except ValueError as e:
        print(f"Product validation error: {e}")
