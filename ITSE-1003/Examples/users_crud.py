# -------------------------------------------------
# File Name: ITSE-1003/Examples/users_crud.py
# Description: CRUD mínimo con SQLAlchemy 2.x y SQLite (tabla users).
#              La base queda en data/users_crud.db (no mezclar con school.db).
# -------------------------------------------------

from __future__ import annotations

from pathlib import Path

import sqlalchemy as sa
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

# --- Rutas y motor -----------------------------------------------------------

_DATA_DIR = Path(__file__).resolve().parent / "data"
_DB_PATH = _DATA_DIR / "users_crud.db"
_DATA_DIR.mkdir(parents=True, exist_ok=True)

engine = sa.create_engine(
    f"sqlite:///{_DB_PATH.resolve().as_posix()}",
    echo=False,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


# --- Modelo ------------------------------------------------------------------


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(sa.String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(sa.String(100), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username!r}, email={self.email!r})>"

    def __str__(self) -> str:
        return f"{self.id}: {self.username} <{self.email}>"


# --- CRUD --------------------------------------------------------------------


def create_user(session: Session, username: str, email: str) -> User:
    """Inserta un usuario. Lanza ValueError si username o email ya existen."""
    user = User(username=username.strip(), email=email.strip())
    session.add(user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise ValueError(
            f"Username o email duplicado: username={username!r}, email={email!r}"
        ) from None
    session.refresh(user)
    print(f"[CREATE] {user}")
    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    user = session.get(User, user_id)
    if user:
        print(f"[READ]   {user}")
    else:
        print(f"[READ]   No hay usuario con id={user_id}")
    return user


def get_user_by_username(session: Session, username: str) -> User | None:
    user = session.scalar(select(User).where(User.username == username.strip()))
    if user:
        print(f"[READ]   {user}")
    else:
        print(f"[READ]   No hay usuario con username={username!r}")
    return user


def get_user_by_email(session: Session, email: str) -> User | None:
    user = session.scalar(select(User).where(User.email == email.strip()))
    if user:
        print(f"[READ]   {user}")
    else:
        print(f"[READ]   No hay usuario con email={email!r}")
    return user


def get_all_users(session: Session) -> list[User]:
    users = list(session.scalars(select(User).order_by(User.id)))
    print(f"[READ]   {len(users)} usuario(s):")
    for user in users:
        print(f"         {user}")
    return users


def update_user(
    session: Session,
    user_id: int,
    *,
    username: str | None = None,
    email: str | None = None,
) -> User | None:
    """Actualiza username y/o email. Argumentos solo por nombre para evitar confusiones."""
    user = session.get(User, user_id)
    if not user:
        print(f"[UPDATE] No hay usuario con id={user_id}")
        return None

    if username is not None:
        user.username = username.strip()
    if email is not None:
        user.email = email.strip()

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print(f"[UPDATE] Violación de unicidad al actualizar id={user_id}")
        return None
    session.refresh(user)
    print(f"[UPDATE] {user}")
    return user


def delete_user(session: Session, user_id: int) -> bool:
    user = session.get(User, user_id)
    if not user:
        print(f"[DELETE] No hay usuario con id={user_id}")
        return False
    session.delete(user)
    session.commit()
    print(f"[DELETE] Usuario id={user_id} eliminado")
    return True


def init_db() -> None:
    """Crea las tablas si no existen."""
    Base.metadata.create_all(engine)


# --- Demo --------------------------------------------------------------------


def main() -> None:
    init_db()

    with SessionLocal() as session:
        print("\n--- CREATE ---")
        arjan = create_user(session, username="Arjan", email="arjan@arjancodes.com")
        floren = create_user(session, username="Florentino", email="florentino@example.com")
        create_user(session, username="Maria", email="maria@example.com")

        print("\n--- READ ALL ---")
        get_all_users(session)

        print("\n--- READ BY ID ---")
        get_user_by_id(session, arjan.id)

        print("\n--- READ BY USERNAME ---")
        get_user_by_username(session, "Florentino")

        print("\n--- READ BY EMAIL ---")
        get_user_by_email(session, "maria@example.com")

        print("\n--- UPDATE ---")
        update_user(session, floren.id, email="florentino@newdomain.com")
        update_user(session, floren.id, username="Florentino_DO")

        print("\n--- DELETE ---")
        delete_user(session, arjan.id)
        delete_user(session, user_id=999)

        print("\n--- READ ALL AFTER DELETE ---")
        get_all_users(session)

        print("\n--- DUPLICATE (IntegrityError -> ValueError) ---")
        try:
            create_user(session, username="Maria", email="otro@example.com")
        except ValueError as e:
            print(f"         Esperado: {e}")


if __name__ == "__main__":
    main()
