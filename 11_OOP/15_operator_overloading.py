# -------------------------------------------------
# File: 15_operator_overloading.py
# Description: Operator overloading with magic methods.
#              __add__, __sub__, __mul__, etc.
# -------------------------------------------------

from typing import Any, Union


class Vector:
    """2D Vector with operator overloading."""

    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __add__(self, other: object) -> Union["Vector", type(NotImplemented)]:
        """Vector addition: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return NotImplemented

    def __sub__(self, other: object) -> Union["Vector", type(NotImplemented)]:
        """Vector subtraction: v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        return NotImplemented

    def __mul__(self, other):
        """Scalar multiplication: v * scalar"""
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        """Right multiplication: scalar * v"""
        return self.__mul__(other)

    def __neg__(self) -> "Vector":
        """Negation: -v"""
        return Vector(-self.x, -self.y)

    def __eq__(self, other: object) -> bool:
        """Equality comparison."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


class ComplexNumber:
    """Complex number with operator overloading."""

    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """Complex addition."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imag)
        return NotImplemented

    def __mul__(self, other: object) -> Union["ComplexNumber", type(NotImplemented)]:
        """Complex multiplication."""
        if isinstance(other, ComplexNumber):
            # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real, imag)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imag * other)
        return NotImplemented

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __repr__(self) -> str:
        return f"ComplexNumber({self.real}, {self.imag})"


class Matrix:
    """Simple 2x2 matrix with operator overloading."""

    def __init__(self, data: list[list[float]]) -> None:
        """data should be 2x2 list of lists."""
        self.data = data

    def __add__(self, other):
        """Matrix addition."""
        if isinstance(other, Matrix):
            result = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    result[i][j] = self.data[i][j] + other.data[i][j]
            return Matrix(result)
        return NotImplemented

    def __mul__(self, other):
        """Matrix multiplication."""
        if isinstance(other, Matrix):
            result = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        result[i][j] += self.data[i][k] * other.data[k][j]
            return Matrix(result)
        return NotImplemented

    def __str__(self):
        return f"Matrix({self.data[0]}, {self.data[1]})"

    def __repr__(self):
        return f"Matrix({self.data})"


# Demonstration
if __name__ == "__main__":
    print("=== Operator Overloading Demo ===\n")

    # Vector operations
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print("Vector operations:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"2 * v1 = {2 * v1}")
    print(f"-v1 = {-v1}")
    print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")

    # Complex number operations
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(1, 2)

    print("\nComplex number operations:")
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")
    print(f"c1 + c2 = {c1 + c2}")
    print(f"c1 * c2 = {c1 * c2}")
    print(f"c1 * 2 = {c1 * 2}")

    # Matrix operations
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])

    print("\nMatrix operations:")
    print(f"m1 = {m1}")
    print(f"m2 = {m2}")
    print(f"m1 + m2 = {m1 + m2}")
    print(f"m1 * m2 = {m1 * m2}")

    print("\n=== Common Operator Methods ===")
    print("__add__     -> +")
    print("__sub__     -> -")
    print("__mul__     -> *")
    print("__truediv__ -> /")
    print("__eq__      -> ==")
    print("__lt__      -> <")
    print("__le__      -> <=")
    print("__gt__      -> >")
    print("__ge__      -> >=")
    print("__neg__     -> - (unary)")
    print("__str__     -> str()")
    print("__repr__    -> repr()")

    print("\n=== Best Practices ===")
    print("- Return NotImplemented for unsupported operations")
    print("- Maintain mathematical properties (commutativity, etc.)")
    print("- Use isinstance() for type checking")
    print("- Implement both __method__ and __rmethod__ for commutativity")
    print("- Make operations intuitive and expected")