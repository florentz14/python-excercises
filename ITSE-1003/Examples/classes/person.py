# -------------------------------------------------
# File Name: ITSE-1003/Examples/person.py
# Description: Modelo Person con Pydantic v2 (Address opcional, validadores, campos computados).
# -------------------------------------------------

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    computed_field,
    field_validator,
)


class Gender(str, Enum):
    male = "Masculino"
    female = "Femenino"
    other = "Otro"


class Address(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    street: str = Field(..., min_length=3)
    city: str = Field(..., min_length=2)
    zip_code: str = Field(
        ...,
        pattern=r"^\d{5}$",
        description="Código postal de 5 dígitos",
    )


class Person(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True,
        validate_assignment=True,
    )

    id: int = Field(..., gt=0, description="ID único incremental")
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    birth_date: date
    gender: Gender

    address: Optional[Address] = None
    tags: List[str] = Field(default_factory=list)
    is_active: bool = True

    @field_validator("birth_date")
    @classmethod
    def birth_date_must_be_in_past(cls, v: date) -> date:
        if v >= date.today():
            raise ValueError("La fecha de nacimiento debe ser en el pasado")
        return v

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @computed_field
    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    @computed_field
    @property
    def formatted_address(self) -> str:
        """Texto de dirección seguro aunque `address` sea None."""
        addr = self.address
        if addr is None:
            return "Sin dirección"
        return f"{addr.street}, {addr.city} ({addr.zip_code})"

    def get_summary(self) -> str:
        status = "Activo" if self.is_active else "Inactivo"
        return (
            f"[{self.id}] {self.full_name} ({self.age} años) - "
            f"Estado: {status} - {self.formatted_address}"
        )


if __name__ == "__main__":
    try:
        raw_data = {
            "id": 50,
            "first_name": "   Roberto  ",
            "last_name": "Gomez",
            "email": "roberto.g@backend.dev",
            "birth_date": "1988-03-15",
            "gender": "Masculino",
            "address": {
                "street": "Avenida Siempre Viva 742",
                "city": "Springfield",
                "zip_code": "12345",
            },
            "tags": ["python", "pydantic", "developer"],
        }

        user = Person(**raw_data)

        print("[OK] Validacion exitosa")
        print(user.get_summary())
        print(f"Correo validado: {user.email}")
        print(f"Direccion: {user.formatted_address}")

        user_sin_dir = Person(
            id=51,
            first_name="Ana",
            last_name="Lopez",
            email="ana@example.com",
            birth_date=date(1995, 6, 1),
            gender=Gender.female,
        )
        print(f"\nSin address: {user_sin_dir.formatted_address}")
        print(user_sin_dir.get_summary())

        print("\nRepresentacion JSON (campos computados incluidos):")
        print(user.model_dump_json(indent=2))

    except Exception as e:
        print(f"[Error] {e}")
