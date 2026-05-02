import numpy as np

print("=" * 50)
print("4. DATA TYPES")
print("=" * 50)

a_int   = np.array([1, 2, 3],       dtype=np.int32)
a_float = np.array([1.1, 2.2, 3.3], dtype=np.float64)
a_bool  = np.array([True, False, True], dtype=np.bool_)
a_str   = np.array(["a", "b", "c"], dtype=np.str_)
casted  = a_int.astype(np.float64)

print(f"int32:   {a_int}   dtype={a_int.dtype}")
print(f"float64: {a_float} dtype={a_float.dtype}")
print(f"bool:    {a_bool}  dtype={a_bool.dtype}")
print(f"str:     {a_str}   dtype={a_str.dtype}")
print(f"int→float cast: {casted} dtype={casted.dtype}")
