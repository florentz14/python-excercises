# -------------------------------------------------
# File Name: ITSE-1003/Examples/oop_13.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Employee class model.
# -------------------------------------------------

from datetime import date

class Employee:
    def __init__(self, emp_id, name, age, salary, department, position, avatar_url=None):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
        self.position = position
        
        # Propiedades automáticas o por defecto
        self.hire_date = date.today()
        self.is_active = True
        self.email = f"{name.lower().replace(' ', '.')}@empresa.com"
        self.skills = []
        
        # Lógica para el avatar_url
        if avatar_url:
            self.avatar_url = avatar_url
        else:
            # Genera un avatar con iniciales si no se provee uno
            nombre_url = name.replace(" ", "+")
            self.avatar_url = f"https://ui-avatars.com/api/?name={nombre_url}&background=random"

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

    def __str__(self):
        status = "Activo" if self.is_active else "Inactivo"
        return (f"[{self.emp_id}] {self.name} - {self.position} ({self.department})\n"
                f"Status: {status} | Avatar: {self.avatar_url}")

    def __repr__(self):
        return f'Employee(name={self.name}, avatar_url={self.avatar_url})'
