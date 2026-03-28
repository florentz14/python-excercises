# -------------------------------------------------
# File Name: ITSE-1003/Examples/diamond_mro.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Multiple inheritance and MRO.
# -------------------------------------------------


class A:
    def action(self) -> str:
        return "A.action"


class B(A):
    def action(self) -> str:
        return "B.action"


class C(A):
    def action(self) -> str:
        return "C.action"


class D(B, C):
    pass


def main() -> None:
    obj = D()
    print("Result:", obj.action())
    print("MRO:", [cls.__name__ for cls in D.__mro__])


if __name__ == "__main__":
    main()
