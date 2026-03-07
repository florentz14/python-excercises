# -------------------------------------------------
# File: 02_init_constructor.py
# Description: Understanding the __init__ constructor method.
#              Initialization, default parameters, validation.
# -------------------------------------------------


class Person:
    """Person class demonstrating constructor usage."""

    def __init__(self, name: str, age: int = 0, city: str = "Unknown") -> None:
        """Constructor with default parameters."""
        self.name: str = name
        self.age: int = age
        self.city: str = city
        print(f"Person {name} created!")

    def introduce(self) -> str:
        """Introduce the person."""
        return f"Hi, I'm {self.name}, {self.age} years old from {self.city}."


class Rectangle:
    """Rectangle class with constructor validation."""

    def __init__(self, width: float, height: float) -> None:
        """Constructor with validation."""
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")

        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        """Calculate area."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate perimeter."""
        return 2 * (self.width + self.height)


class BankAccount:
    """Bank account with constructor that sets initial state."""

    def __init__(self, account_number: str, owner: str, initial_balance: float = 0) -> None:
        """Constructor setting up account state."""
        self.account_number: str = account_number
        self.owner: str = owner
        self.balance: float = initial_balance
        self.transactions: list[str] = []

        # Record initial deposit if any
        if initial_balance > 0:
            self.transactions.append(f"Initial deposit: ${initial_balance}")

    def deposit(self, amount: float) -> None:
        """Deposit money."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")

    def get_balance(self) -> float:
        """Get current balance."""
        return self.balance


# Demonstration
if __name__ == "__main__":
    print("=== Constructor Examples ===\n")

    # Person with different constructor calls
    person1 = Person("Alice", 25, "New York")
    person2 = Person("Bob", 30)  # Using default city
    person3 = Person("Charlie")   # Using all defaults

    print(person1.introduce())
    print(person2.introduce())
    print(person3.introduce())

    print("\n=== Rectangle with Validation ===")
    try:
        rect = Rectangle(5, 3)
        print(f"Rectangle: {rect.width}x{rect.height}")
        print(f"Area: {rect.area()}")
        print(f"Perimeter: {rect.perimeter()}")

        # This will raise an error
        bad_rect = Rectangle(-1, 5)
    except ValueError as e:
        print(f"Error: {e}")

    print("\n=== Bank Account Constructor ===")
    account = BankAccount("123456", "John Doe", 1000)
    print(f"Account {account.account_number} for {account.owner}")
    print(f"Initial balance: ${account.get_balance()}")

    account.deposit(500)
    print(f"After deposit: ${account.get_balance()}")
