# -------------------------------------------------
# File Name: ITSE-1003/Examples/sales/sales_models.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: SQLAlchemy ORM — clientes, suplidores, productos, inventario, facturas y líneas.
# -------------------------------------------------

from __future__ import annotations

from datetime import date
from typing import List, Optional

from sqlalchemy import Date, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


_money = Numeric(12, 2, asdecimal=False)
_tax = Numeric(8, 6, asdecimal=False)


class Supplier(Base):
    """Suplidor de mercancía."""

    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(160), nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String(40))
    email: Mapped[Optional[str]] = mapped_column(String(120))
    notes: Mapped[Optional[str]] = mapped_column(Text())

    products: Mapped[List["Product"]] = relationship(back_populates="supplier")


class Customer(Base):
    """Cliente (comprador)."""

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(160), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(120))
    phone: Mapped[Optional[str]] = mapped_column(String(40))

    invoices: Mapped[List["Invoice"]] = relationship(back_populates="customer")


class Product(Base):
    """Artículo / producto vendible."""

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sku: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    unit_price: Mapped[float] = mapped_column(_money, nullable=False)
    supplier_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("suppliers.id", ondelete="SET NULL"),
    )
    is_active: Mapped[bool] = mapped_column(default=True)

    supplier: Mapped[Optional[Supplier]] = relationship(back_populates="products")
    inventory: Mapped[Optional["Inventory"]] = relationship(
        back_populates="product",
        uselist=False,
        cascade="all, delete-orphan",
    )


class Inventory(Base):
    """Existencias por producto (una fila por artículo)."""

    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )
    quantity_on_hand: Mapped[int] = mapped_column(default=0, nullable=False)

    product: Mapped[Product] = relationship(back_populates="inventory")


class Invoice(Base):
    """Factura (cabecera)."""

    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    invoice_number: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)
    invoice_date: Mapped[date] = mapped_column(Date, nullable=False)
    tax_rate: Mapped[float] = mapped_column(_tax, default=0.0)
    status: Mapped[str] = mapped_column(String(20), default="borrador")
    currency: Mapped[str] = mapped_column(String(3), default="USD")
    subtotal: Mapped[float] = mapped_column(_money, default=0.0)
    tax_amount: Mapped[float] = mapped_column(_money, default=0.0)
    grand_total: Mapped[float] = mapped_column(_money, default=0.0)

    customer: Mapped[Customer] = relationship(back_populates="invoices")
    lines: Mapped[List["InvoiceLine"]] = relationship(
        back_populates="invoice",
        cascade="all, delete-orphan",
    )


class InvoiceLine(Base):
    """Línea de factura (detalle)."""

    __tablename__ = "invoice_lines"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    unit_price: Mapped[float] = mapped_column(_money, nullable=False)

    invoice: Mapped[Invoice] = relationship(back_populates="lines")
    product: Mapped[Product] = relationship()


def recalculate_invoice_totals(invoice: Invoice) -> None:
    """Actualiza subtotal, impuesto y total a partir de las líneas."""
    sub = sum(float(ln.quantity) * float(ln.unit_price) for ln in invoice.lines)
    tax = sub * float(invoice.tax_rate)
    invoice.subtotal = round(sub, 2)
    invoice.tax_amount = round(tax, 2)
    invoice.grand_total = round(sub + tax, 2)
