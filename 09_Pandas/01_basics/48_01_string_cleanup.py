text = "foo,  bar, \t baz,  qux"
pieces = [value.strip() for value in text.split(",")]

print("Cleaned pieces:")
print(pieces)
