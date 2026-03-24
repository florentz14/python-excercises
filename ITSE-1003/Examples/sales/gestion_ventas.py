# -------------------------------------------------
# File Name: ITSE-1003/Examples/sales/gestion_ventas.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Menú sencillo — ventas, facturación, clientes, productos, suplidores e inventario (SQLite + SQLAlchemy).
# -------------------------------------------------

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

_examples_dir = Path(__file__).resolve().parent.parent
_pkg_dir = Path(__file__).resolve().parent
if str(_examples_dir) not in sys.path:
    sys.path.insert(0, str(_examples_dir))
if str(_pkg_dir) not in sys.path:
    sys.path.insert(0, str(_pkg_dir))

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from tabulate import tabulate

from sales_database import (
    finalize_invoice,
    get_session,
    init_db,
    mark_invoice_paid,
    next_invoice_number,
    seed_sample_data,
    session_scope,
)
from sales_models import (
    Customer,
    Inventory,
    Invoice,
    InvoiceLine,
    Product,
    Supplier,
    recalculate_invoice_totals,
)


def _prompt(msg: str, default: str | None = None) -> str:
    if default is not None:
        raw = input(f"{msg} [{default}]: ").strip()
        return raw if raw else default
    return input(f"{msg}: ").strip()


def _prompt_float(msg: str, default: float) -> float:
    s = _prompt(msg, str(default))
    try:
        return float(s.replace(",", "."))
    except ValueError:
        return default


def _prompt_int(msg: str, default: int | None = None) -> int | None:
    s = _prompt(msg, str(default) if default is not None else "")
    if not s:
        return default
    try:
        return int(s)
    except ValueError:
        return default


def _table(rows: list[list[object]], headers: list[str]) -> None:
    print(tabulate(rows, headers=headers, tablefmt="grid"))


# Filas del menú principal: dos pares (opción / descripción) por línea.
_MAIN_MENU_ROWS: list[list[str]] = [
    ["1", "Listar clientes", "2", "Alta cliente"],
    ["3", "Listar suplidores", "4", "Alta suplidor"],
    ["5", "Listar productos", "6", "Alta producto"],
    ["7", "Inventario (ver existencias)", "8", "Ajustar existencia"],
    ["9", "Nueva factura (borrador)", "", ""],
    ["10", "Listar facturas", "11", "Ver detalle factura"],
    ["12", "Finalizar factura", "13", "Marcar factura pagada"],
    ["14", "Recargar datos demo (si no hay suplidores)", "", ""],
    ["0", "Salir", "99", "Reiniciar base de datos"],
]


def print_main_menu() -> None:
    print(
        tabulate(
            _MAIN_MENU_ROWS,
            headers=["Opc.", "Descripcion", "Opc.", "Descripcion"],
            tablefmt="grid",
            stralign="left",
        )
    )


def cmd_reset_db() -> None:
    if _prompt("¿Borrar toda la BD y volver a crear? (s/N)", "N").lower() != "s":
        return
    init_db(drop_all=True)
    with session_scope() as s:
        seed_sample_data(s)
    print("Base reiniciada con datos de ejemplo.")


def list_customers(session: Session) -> None:
    rows = session.scalars(select(Customer).order_by(Customer.id)).all()
    data = [[c.id, c.name, c.email or "", c.phone or ""] for c in rows]
    _table(data, ["id", "nombre", "email", "teléfono"])


def add_customer(session: Session) -> None:
    name = _prompt("Nombre del cliente")
    if not name:
        print("Cancelado.")
        return
    email = _prompt("Email (opcional)", "") or None
    phone = _prompt("Teléfono (opcional)", "") or None
    session.add(Customer(name=name, email=email, phone=phone))
    session.commit()
    print("Cliente guardado.")


def list_suppliers(session: Session) -> None:
    rows = session.scalars(select(Supplier).order_by(Supplier.id)).all()
    data = [[s.id, s.name, s.phone or "", s.email or ""] for s in rows]
    _table(data, ["id", "nombre", "teléfono", "email"])


def add_supplier(session: Session) -> None:
    name = _prompt("Nombre del suplidor")
    if not name:
        print("Cancelado.")
        return
    phone = _prompt("Teléfono (opcional)", "") or None
    email = _prompt("Email (opcional)", "") or None
    session.add(Supplier(name=name, phone=phone, email=email))
    session.commit()
    print("Suplidor guardado.")


def list_products(session: Session) -> None:
    rows = session.scalars(
        select(Product).options(joinedload(Product.inventory)).order_by(Product.id)
    ).all()
    data = []
    for p in rows:
        stock = p.inventory.quantity_on_hand if p.inventory else 0
        data.append([p.id, p.sku, p.name, f"{float(p.unit_price):.2f}", p.supplier_id or "", stock])
    _table(data, ["id", "sku", "nombre", "precio", "suplidor_id", "existencia"])


def add_product(session: Session) -> None:
    sku = _prompt("SKU")
    name = _prompt("Nombre del artículo")
    if not sku or not name:
        print("Cancelado.")
        return
    price = _prompt_float("Precio unitario", 0.0)
    list_suppliers(session)
    sid = _prompt_int("ID suplidor (Enter = ninguno)", None)
    supplier_id = sid if sid else None
    stock = _prompt_int("Existencia inicial", 0) or 0
    p = Product(sku=sku, name=name, unit_price=price, supplier_id=supplier_id)
    session.add(p)
    session.flush()
    session.add(Inventory(product_id=p.id, quantity_on_hand=stock))
    session.commit()
    print("Producto e inventario inicial guardados.")


def list_inventory(session: Session) -> None:
    rows = session.scalars(
        select(Inventory).options(joinedload(Inventory.product)).order_by(Inventory.product_id)
    ).all()
    data = [
        [r.product_id, r.product.sku, r.product.name, r.quantity_on_hand]
        for r in rows
        if r.product
    ]
    _table(data, ["producto_id", "sku", "nombre", "existencia"])


def adjust_inventory(session: Session) -> None:
    list_inventory(session)
    pid = _prompt_int("ID de producto a ajustar")
    if pid is None:
        return
    row = session.scalars(select(Inventory).where(Inventory.product_id == pid)).first()
    if row is None:
        print("No hay registro de inventario para ese producto.")
        return
    q = _prompt_int("Nueva existencia (cantidad absoluta)", row.quantity_on_hand)
    if q is None:
        return
    row.quantity_on_hand = max(0, q)
    session.commit()
    print("Inventario actualizado.")


def new_invoice_draft(session: Session) -> None:
    list_customers(session)
    cid = _prompt_int("ID del cliente")
    if cid is None:
        return
    if session.get(Customer, cid) is None:
        print("Cliente inválido.")
        return
    tax = _prompt_float("Tasa de impuesto (ej. 0.08 para 8%)", 0.08)
    inv = Invoice(
        invoice_number=next_invoice_number(session),
        customer_id=cid,
        invoice_date=date.today(),
        tax_rate=tax,
        status="borrador",
    )
    session.add(inv)
    session.flush()
    print(f"Factura borrador #{inv.id} — {inv.invoice_number}")
    while True:
        list_products(session)
        pid = _prompt_int("ID producto para agregar línea (0 = terminar)", 0)
        if pid is None or pid == 0:
            break
        prod = session.get(Product, pid)
        if prod is None or not prod.is_active:
            print("Producto no válido.")
            continue
        qty = _prompt_int("Cantidad", 1) or 1
        if qty < 1:
            continue
        price = _prompt_float("Precio unitario (Enter = precio de lista)", float(prod.unit_price))
        session.add(
            InvoiceLine(
                invoice_id=inv.id,
                product_id=prod.id,
                quantity=qty,
                unit_price=price,
            )
        )
        session.flush()
        print("Línea agregada.")
    session.refresh(inv)
    recalculate_invoice_totals(inv)
    session.commit()
    print("Borrador guardado. Use 'Finalizar factura' para descontar inventario.")


def list_invoices(session: Session) -> None:
    rows = session.scalars(
        select(Invoice).options(joinedload(Invoice.customer)).order_by(Invoice.id.desc())
    ).all()
    data = [
        [
            i.id,
            i.invoice_number,
            i.customer.name,
            i.invoice_date,
            i.status,
            f"{float(i.grand_total):.2f}",
            i.currency,
        ]
        for i in rows
    ]
    _table(data, ["id", "número", "cliente", "fecha", "estado", "total", "moneda"])


def show_invoice(session: Session) -> None:
    iid = _prompt_int("ID de factura")
    if iid is None:
        return
    inv = session.scalars(
        select(Invoice)
        .options(
            joinedload(Invoice.customer),
            joinedload(Invoice.lines).joinedload(InvoiceLine.product),
        )
        .where(Invoice.id == iid)
    ).first()
    if inv is None:
        print("No existe.")
        return
    print(f"\n{inv.invoice_number} | {inv.customer.name} | {inv.invoice_date} | {inv.status}")
    print(f"Subtotal: {float(inv.subtotal):.2f}  Impuesto: {float(inv.tax_amount):.2f}  Total: {float(inv.grand_total):.2f} {inv.currency}")
    lines_data = [
        [ln.id, ln.product.sku, ln.product.name, ln.quantity, f"{float(ln.unit_price):.2f}"]
        for ln in inv.lines
    ]
    _table(lines_data, ["línea_id", "sku", "descripción", "cant.", "p.unit."])


def do_finalize(session: Session) -> None:
    list_invoices(session)
    iid = _prompt_int("ID factura a finalizar")
    if iid is None:
        return
    try:
        finalize_invoice(session, iid)
        session.commit()
        print("Factura finalizada e inventario actualizado.")
    except ValueError as e:
        session.rollback()
        print(f"Error: {e}")


def do_mark_paid(session: Session) -> None:
    list_invoices(session)
    iid = _prompt_int("ID factura a marcar pagada")
    if iid is None:
        return
    try:
        mark_invoice_paid(session, iid)
        session.commit()
        print("Estado: pagada.")
    except ValueError as e:
        session.rollback()
        print(f"Error: {e}")


def main() -> None:
    print("=== Gestión de ventas (SQLite + SQLAlchemy) ===\n")
    init_db(drop_all=False)
    with session_scope() as s:
        seed_sample_data(s)

    while True:
        print()
        print_main_menu()
        op = _prompt("Opción", "0")
        session = get_session()
        try:
            if op == "0":
                break
            if op == "1":
                list_customers(session)
            elif op == "2":
                add_customer(session)
            elif op == "3":
                list_suppliers(session)
            elif op == "4":
                add_supplier(session)
            elif op == "5":
                list_products(session)
            elif op == "6":
                add_product(session)
            elif op == "7":
                list_inventory(session)
            elif op == "8":
                adjust_inventory(session)
            elif op == "9":
                new_invoice_draft(session)
            elif op == "10":
                list_invoices(session)
            elif op == "11":
                show_invoice(session)
            elif op == "12":
                do_finalize(session)
            elif op == "13":
                do_mark_paid(session)
            elif op == "14":
                seed_sample_data(session)
                session.commit()
                print("Hecho (no duplica si ya hay suplidores).")
            elif op == "99":
                cmd_reset_db()
            else:
                print("Opción no válida. (99 = reiniciar BD)")
        finally:
            session.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAdiós.")
        sys.exit(0)
