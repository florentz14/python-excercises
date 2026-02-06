# dataclass_inventory.py
# Function using type hints and dataclass

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Product:
    """
    Represents a product in inventory.
    
    Attributes:
        name: Product name
        price: Unit price
        quantity: Stock quantity (default 0)
        category: Optional category
    """
    name: str
    price: float
    quantity: int = 0
    category: Optional[str] = None
    
    def total_value(self) -> float:
        """Returns total value of this product in stock."""
        return self.price * self.quantity
    
    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f} x {self.quantity})"


@dataclass
class Customer:
    """
    Represents a customer.
    
    Attributes:
        name: Customer name
        email: Customer email
        purchases: List of purchased products
    """
    name: str
    email: str
    purchases: List[Product] = field(default_factory=list)
    
    def total_spent(self) -> float:
        """Returns total amount spent by customer."""
        return sum(p.price for p in self.purchases)


def calculate_inventory_value(products: List[Product]) -> dict[str, float]:
    """
    Calculates total inventory value with type hints.
    
    Args:
        products: List of Product objects
        
    Returns:
        Dictionary with total and average values
    """
    if not products:
        return {'total': 0.0, 'average': 0.0, 'items': 0}
    
    total = sum(p.price * p.quantity for p in products)
    total_items = sum(p.quantity for p in products)
    average = total / len(products)
    
    return {
        'total': total,
        'average': average,
        'items': total_items
    }


def filter_by_category(products: List[Product], category: str) -> List[Product]:
    """
    Filters products by category.
    
    Args:
        products: List of products
        category: Category to filter by
        
    Returns:
        List of products in the specified category
    """
    return [p for p in products if p.category == category]


def low_stock_products(products: List[Product], threshold: int = 5) -> List[Product]:
    """
    Returns products with stock below threshold.
    
    Args:
        products: List of products
        threshold: Minimum stock level (default 5)
        
    Returns:
        List of products with low stock
    """
    return [p for p in products if p.quantity < threshold]


# Example usage
if __name__ == "__main__":
    print("=== Dataclass & Type Hints Demo ===\n")
    
    # Create products
    products = [
        Product("Laptop", 999.99, 5, "Electronics"),
        Product("Mouse", 29.99, 20, "Electronics"),
        Product("Keyboard", 79.99, 10, "Electronics"),
        Product("Notebook", 4.99, 50, "Office"),
        Product("Pen", 1.99, 100, "Office"),
        Product("Monitor", 299.99, 3, "Electronics"),
    ]
    
    # Display products
    print("1. Product inventory:")
    for p in products:
        print(f"   {p} = ${p.total_value():.2f}")
    
    print()
    
    # Calculate inventory value
    print("2. Inventory summary:")
    summary = calculate_inventory_value(products)
    print(f"   Total value: ${summary['total']:.2f}")
    print(f"   Average per product: ${summary['average']:.2f}")
    print(f"   Total items: {summary['items']}")
    
    print()
    
    # Filter by category
    print("3. Electronics products:")
    electronics = filter_by_category(products, "Electronics")
    for p in electronics:
        print(f"   {p}")
    
    print()
    
    # Low stock alert
    print("4. Low stock products (< 5 units):")
    low = low_stock_products(products)
    for p in low:
        print(f"   WARNING: {p.name} - only {p.quantity} left!")
    
    print()
    
    # Customer example
    print("5. Customer with purchases:")
    customer = Customer(
        name="John Doe",
        email="john@example.com",
        purchases=[products[0], products[1], products[3]]
    )
    print(f"   Customer: {customer.name}")
    print(f"   Email: {customer.email}")
    print(f"   Purchases: {len(customer.purchases)} items")
    print(f"   Total spent: ${customer.total_spent():.2f}")
