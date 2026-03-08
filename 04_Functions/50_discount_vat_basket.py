# -------------------------------------------------
# File Name: 50_discount_vat_basket.py
# Description: Discount, VAT, and basket with function application
# -------------------------------------------------

from typing import Callable


def apply_discount(price: float, percent: float) -> float:
    """Apply discount to price. percent in 0-100."""
    return price * (1 - percent / 100)


def apply_vat(price: float, percent: float) -> float:
    """Apply VAT to price. percent in 0-100."""
    return price * (1 + percent / 100)


def basket_total(
    basket: dict[str, tuple[float, float]],
    modifier: Callable[[float, float], float]
) -> float:
    """
    basket: {product: (price, percent)}
    modifier: apply_discount or apply_vat
    Returns final total.
    """
    return sum(modifier(price, pct) for price, pct in basket.values())


if __name__ == "__main__":
    # Example: product -> (price, discount_or_vat_percent)
    basket_discount = {"apple": (2.00, 10), "bread": (1.50, 5), "milk": (1.20, 0)}
    basket_vat = {"apple": (2.00, 21), "bread": (1.50, 21), "milk": (1.20, 21)}

    print("Basket with 10%/5%/0% discount:", basket_total(basket_discount, apply_discount))
    print("Basket with 21% VAT:", basket_total(basket_vat, apply_vat))
