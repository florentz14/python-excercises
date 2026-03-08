# -------------------------------------------------
# File Name: 19_namedtuple_intro.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Introduction to namedtuple for named field access.
# -------------------------------------------------

from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
p = Person("Anna", 30)

print("Person:", p)
print("p.name:", p.name)
print("p.age:", p.age)
print("p[0]:", p[0])
