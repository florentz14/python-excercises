# ------------------------------------------------------------
# File: 19_namedtuple_intro.py
# Purpose: Introduction to namedtuple.
# Description: Named fields for readable tuple access.
# ------------------------------------------------------------

from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
p = Person("Anna", 30)

print("Person:", p)
print("p.name:", p.name)
print("p.age:", p.age)
print("p[0]:", p[0])
