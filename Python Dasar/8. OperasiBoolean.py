"""
OPERASI LOGIKA / BOOLEAN

- not
- or
- and
- xor
"""

# NOT (Membalikkan)
print("===NOT===")
a = True
b = not a
print(f"Data a = {a}")
print(f"Data b = {b}")

# OR (Jika salah satu True, maka hasilnya True)
print("===OR===")
a = False
b = False
c = a or b
print(f"{a} OR {b} = {c}")
a = False
b = True
c = a or b
print(f"{a} OR {b}  = {c}")
a = True
b = False
c = a or b
print(f"{a} OR {b}  = {c}")
a = True
b = True
c = a or b
print(f"{a} OR {b}   = {c}")

# AND (Jika keduanya True, maka hasilnya akan True)
print("===AND===")
a = False
b = False
c = a and b
print(f"{a} and {b} = {c}")
a = False
b = True
c = a and b
print(f"{a} and {b}  = {c}")
a = True
b = False
c = a and b
print(f"{a} and {b}  = {c}")
a = True
b = True
c = a and b
print(f"{a} and {b}   = {c}")

# XOR (Jika salah satu nilai True, maka hasilnya akan True)
print("===XOR===")
a = False
b = False
c = a ^ b
print(f"{a} ^ {b} = {c}")
a = False
b = True
c = a ^ b
print(f"{a} ^ {b}  = {c}")
a = True
b = False
c = a ^ b
print(f"{a} ^ {b}  = {c}")
a = True
b = True
c = a ^ b
print(f"{a} ^ {b}   = {c}")