# -------------------------------------------------
# File: 20_composition.py
# Description: Composition vs inheritance.
#              Building objects from other objects.
# -------------------------------------------------

from typing import List
import datetime


class Engine:
    """Car engine component."""

    def __init__(self, horsepower: int, fuel_type: str = "gasoline"):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False

    def start(self):
        """Start the engine."""
        self.is_running = True
        return f"Engine started ({self.horsepower} HP {self.fuel_type})"

    def stop(self):
        """Stop the engine."""
        self.is_running = False
        return "Engine stopped"

    def get_status(self):
        """Get engine status."""
        return f"Engine is {'running' if self.is_running else 'stopped'}"


class Transmission:
    """Car transmission component."""

    def __init__(self, type_: str = "automatic", gears: int = 6):
        self.type_ = type_
        self.gears = gears
        self.current_gear = 1

    def shift_gear(self, gear: int):
        """Shift to a specific gear."""
        if 1 <= gear <= self.gears:
            self.current_gear = gear
            return f"Shifted to gear {gear}"
        return f"Invalid gear. Must be between 1 and {self.gears}"

    def get_info(self):
        """Get transmission info."""
        return f"{self.type_.capitalize()} transmission, {self.gears} gears, current: {self.current_gear}"


class Wheels:
    """Car wheels component."""

    def __init__(self, size: int, tire_type: str = "all-season"):
        self.size = size  # in inches
        self.tire_type = tire_type
        self.pressure = 32  # PSI

    def inflate(self, psi: int):
        """Inflate tires."""
        self.pressure += psi
        return f"Tires inflated to {self.pressure} PSI"

    def get_info(self):
        """Get wheel info."""
        return f"{self.size}\" wheels with {self.tire_type} tires ({self.pressure} PSI)"


class GPS:
    """GPS navigation system."""

    def __init__(self):
        self.current_location = "Home"
        self.destination = None

    def set_destination(self, location: str):
        """Set navigation destination."""
        self.destination = location
        return f"Destination set to {location}"

    def get_directions(self):
        """Get directions to destination."""
        if not self.destination:
            return "No destination set"
        return f"Directions from {self.current_location} to {self.destination}"

    def update_location(self, location: str):
        """Update current location."""
        self.current_location = location
        return f"Location updated to {location}"


class Car:
    """Car composed of multiple components."""

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

        # Composition: Car has components
        self.engine = Engine(200, "gasoline")
        self.transmission = Transmission("automatic", 6)
        self.wheels = Wheels(17, "performance")
        self.gps = GPS()

    def start(self):
        """Start the car."""
        return self.engine.start()

    def drive(self):
        """Drive the car."""
        if not self.engine.is_running:
            return "Cannot drive: engine is not running"
        return f"Driving {self.year} {self.make} {self.model}"

    def get_status(self):
        """Get car status."""
        return f"{self.year} {self.make} {self.model}\n" \
            f"Engine: {self.engine.get_status()}\n" \
            f"Transmission: {self.transmission.get_info()}\n" \
            f"Wheels: {self.wheels.get_info()}"

    def navigate_to(self, destination: str):
        """Navigate to destination."""
        return self.gps.set_destination(destination)


class Person:
    """Person with address (composition)."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.address = None  # Will be composed later

    def set_address(self, street: str, city: str, state: str, zip_code: str):
        """Set person's address."""
        self.address = Address(street, city, state, zip_code)

    def get_info(self):
        """Get person info."""
        info = f"Name: {self.name}, Age: {self.age}"
        if self.address:
            info += f"\nAddress: {self.address.get_full_address()}"
        return info


class Address:
    """Address component."""

    def __init__(self, street: str, city: str, state: str, zip_code: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get_full_address(self):
        """Get full address string."""
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"


class Computer:
    """Computer composed of components."""

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

        # Composition
        self.cpu = CPU("Intel i7", 8, 3.2)
        self.memory = Memory(16, "DDR4")
        self.storage = Storage(512, "SSD")
        self.gpu = GPU("NVIDIA RTX 3060", 8)

    def get_specs(self):
        """Get computer specifications."""
        return f"{self.brand} {self.model}\n" \
            f"CPU: {self.cpu.get_info()}\n" \
            f"Memory: {self.memory.get_info()}\n" \
            f"Storage: {self.storage.get_info()}\n" \
            f"GPU: {self.gpu.get_info()}"

    def upgrade_memory(self, additional_gb: int):
        """Upgrade memory."""
        self.memory.add_ram(additional_gb)
        return f"Memory upgraded to {self.memory.capacity}GB"


class CPU:
    """CPU component."""

    def __init__(self, model: str, cores: int, speed_ghz: float):
        self.model = model
        self.cores = cores
        self.speed_ghz = speed_ghz

    def get_info(self):
        return f"{self.model}, {self.cores} cores @ {self.speed_ghz}GHz"


class Memory:
    """Memory component."""

    def __init__(self, capacity_gb: int, type_: str):
        self.capacity = capacity_gb
        self.type_ = type_

    def add_ram(self, additional_gb: int):
        """Add more RAM."""
        self.capacity += additional_gb

    def get_info(self):
        return f"{self.capacity}GB {self.type_}"


class Storage:
    """Storage component."""

    def __init__(self, capacity_gb: int, type_: str):
        self.capacity = capacity_gb
        self.type_ = type_

    def get_info(self):
        return f"{self.capacity}GB {self.type_}"


class GPU:
    """GPU component."""

    def __init__(self, model: str, memory_gb: int):
        self.model = model
        self.memory_gb = memory_gb

    def get_info(self):
        return f"{self.model}, {self.memory_gb}GB VRAM"


class Library:
    """Library with books (composition)."""

    def __init__(self, name: str):
        self.name = name
        self.books = []  # List of Book objects

    def add_book(self, title: str, author: str, isbn: str):
        """Add a book to the library."""
        book = Book(title, author, isbn)
        self.books.append(book)
        return f"Added: {book.get_info()}"

    def find_book(self, title: str):
        """Find a book by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.get_info()
        return "Book not found"

    def get_all_books(self):
        """Get list of all books."""
        return [book.get_info() for book in self.books]


class Book:
    """Book component."""

    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False
        self.due_date = None

    def check_out(self):
        """Check out the book."""
        if not self.checked_out:
            self.checked_out = True
            self.due_date = datetime.date.today() + datetime.timedelta(days=14)
            return f"Checked out. Due: {self.due_date}"
        return "Book is already checked out"

    def check_in(self):
        """Check in the book."""
        if self.checked_out:
            self.checked_out = False
            self.due_date = None
            return "Book checked in"
        return "Book was not checked out"

    def get_info(self):
        """Get book info."""
        status = "Available" if not self.checked_out else f"Due: {self.due_date}"
        return f"'{self.title}' by {self.author} ({status})"


# Demonstration
if __name__ == "__main__":
    print("=== Composition Demo ===\n")

    # Car composition
    print("Car composition:")
    car = Car("Toyota", "Camry", 2022)
    print(car.start())
    print(car.drive())
    print("\nCar status:")
    print(car.get_status())
    print(f"\nNavigation: {car.navigate_to('Work')}")

    # Person with address
    print("\nPerson with address:")
    person = Person("Alice Johnson", 28)
    person.set_address("123 Oak Street", "Springfield", "IL", "62701")
    print(person.get_info())

    # Computer composition
    print("\nComputer composition:")
    computer = Computer("Dell", "XPS 13")
    print("Original specs:")
    print(computer.get_specs())
    print(f"\nUpgrade: {computer.upgrade_memory(8)}")

    # Library with books
    print("\nLibrary composition:")
    library = Library("City Library")
    library.add_book("1984", "George Orwell", "978-0451524935")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
    library.add_book("The Great Gatsby",
                     "F. Scott Fitzgerald", "978-0743273565")

    print("All books:")
    for book_info in library.get_all_books():
        print(f"  {book_info}")

    print(f"\nFinding book: {library.find_book('1984')}")

    # Book checkout
    book_1984 = library.books[0]
    print(f"\nCheckout: {book_1984.check_out()}")
    print(f"Book status: {book_1984.get_info()}")
    print(f"Checkin: {book_1984.check_in()}")
    print(f"Book status: {book_1984.get_info()}")

    print("\n=== Composition vs Inheritance ===")
    print("Composition: 'has-a' relationship")
    print("- Car has an Engine, Transmission, Wheels")
    print("- Person has an Address")
    print("- Library has Books")
    print("- More flexible than inheritance")
    print("- Easier to change at runtime")
    print("- Avoids deep inheritance hierarchies")

    print("\nInheritance: 'is-a' relationship")
    print("- Dog is an Animal")
    print("- Car is a Vehicle")
    print("- Circle is a Shape")
    print("- Better for shared behavior/interfaces")

    print("\n=== When to Use Composition ===")
    print("- Complex objects made of simpler parts")
    print("- Want to reuse components in different contexts")
    print("- Need to change behavior at runtime")
    print("- Avoid tight coupling of inheritance")
    print("- Model real-world 'has-a' relationships")

    print("\n=== Composition Benefits ===")
    print("- Flexibility: Change components independently")
    print("- Reusability: Components can be used elsewhere")
    print("- Testability: Test components separately")
    print("- Maintainability: Changes don't affect other parts")
    print("- Runtime changes: Swap components dynamically")
