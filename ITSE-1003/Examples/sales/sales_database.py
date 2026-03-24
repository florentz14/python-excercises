# -------------------------------------------------
# File Name: ITSE-1003/Examples/sales/sales_database.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: SQLite + SQLAlchemy — motor, sesión, crear tablas y datos de ejemplo.
# -------------------------------------------------

from __future__ import annotations

import sys
from contextlib import contextmanager
from datetime import date
from pathlib import Path
from typing import Generator, Optional

from sqlalchemy import create_engine, func, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

_examples_dir = Path(__file__).resolve().parent.parent
if str(_examples_dir) not in sys.path:
    sys.path.append(str(_examples_dir))

from examples_paths import SALES_DB, SALES_DATA_DIR

from sales_models import (
    Base,
    Customer,
    Inventory,
    Invoice,
    Product,
    Supplier,
    recalculate_invoice_totals,
)


def finalize_invoice(session: Session, invoice_id: int) -> None:
    """Calcula totales, descuenta inventario y pasa la factura a *finalizada*."""
    inv = session.get(Invoice, invoice_id)
    if inv is None:
        raise ValueError("Factura no encontrada.")
    if inv.status != "borrador":
        raise ValueError("Solo se pueden finalizar facturas en borrador.")
    if not inv.lines:
        raise ValueError("Agregue al menos una línea antes de finalizar.")
    recalculate_invoice_totals(inv)
    for ln in inv.lines:
        row = session.scalars(
            select(Inventory).where(Inventory.product_id == ln.product_id)
        ).first()
        if row is None:
            raise ValueError(f"El producto id={ln.product_id} no tiene inventario.")
        if row.quantity_on_hand < ln.quantity:
            sku = ln.product.sku if ln.product else str(ln.product_id)
            raise ValueError(
                f"Stock insuficiente ({sku}): disponible {row.quantity_on_hand}, "
                f"solicitado {ln.quantity}."
            )
    for ln in inv.lines:
        row = session.scalars(
            select(Inventory).where(Inventory.product_id == ln.product_id)
        ).first()
        assert row is not None
        row.quantity_on_hand -= ln.quantity
    inv.status = "finalizada"


def mark_invoice_paid(session: Session, invoice_id: int) -> None:
    inv = session.get(Invoice, invoice_id)
    if inv is None:
        raise ValueError("Factura no encontrada.")
    if inv.status != "finalizada":
        raise ValueError("La factura debe estar finalizada antes de marcarla pagada.")
    inv.status = "pagada"

_engine: Optional[Engine] = None
_SessionLocal: Optional[sessionmaker[Session]] = None


def get_engine(*, echo: bool = False) -> Engine:
    global _engine, _SessionLocal
    if _engine is None:
        SALES_DATA_DIR.mkdir(parents=True, exist_ok=True)
        url = f"sqlite:///{SALES_DB.resolve().as_posix()}"
        _engine = create_engine(
            url,
            echo=echo,
            connect_args={"check_same_thread": False},
        )
        _SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=_engine,
            expire_on_commit=False,
        )
    return _engine


def get_session() -> Session:
    get_engine()
    assert _SessionLocal is not None
    return _SessionLocal()


@contextmanager
def session_scope() -> Generator[Session, None, None]:
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_db(*, drop_all: bool = False, echo: bool = False) -> None:
    engine = get_engine(echo=echo)
    if drop_all:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def seed_sample_data(session: Session) -> None:
    """Inserta suplidores, clientes, productos e inventario si la BD está vacía."""
    n = session.scalar(select(func.count()).select_from(Supplier))
    if (n or 0) > 0:
        return

    s1 = Supplier(name="Distribuidora Norte", phone="809-555-0100", email="ventas@norte.example")
    s2 = Supplier(name="Importadora Central", phone="809-555-0200", email="info@central.example")
    session.add_all([s1, s2])
    session.flush()

    session.add_all(
        [
            Customer(name="Comercial ABC", email="compras@abc.example", phone="809-555-1001"),
            Customer(name="Taller Rápido", email="taller@rapido.example", phone="809-555-1002"),
            Customer(name="Retail Gamma", email="pedidos@gamma.example"),
        ]
    )
    session.flush()

    products_spec = [
        ("SKU-001", "Tornillo hexagonal M8 (caja)", 12.50, s1.id, 200),
        ("SKU-002", "Cable eléctrico 2m", 8.75, s1.id, 150),
        ("SKU-003", "Filtro de aceite A1", 45.00, s2.id, 40),
        ("SKU-004", "Aceite sintético 1L", 22.30, s2.id, 80),
        ("SKU-005", "Kit herramientas básico", 189.99, s1.id, 25),
    ]
    for sku, name, price, sup_id, stock in products_spec:
        p = Product(sku=sku, name=name, unit_price=price, supplier_id=sup_id)
        session.add(p)
        session.flush()
        session.add(Inventory(product_id=p.id, quantity_on_hand=stock))

    session.flush()


def next_invoice_number(session: Session) -> str:
    year = date.today().year
    cnt = session.scalar(select(func.count()).select_from(Invoice))
    seq = (cnt or 0) + 1
    return f"INV-{year}-{seq:04d}"
