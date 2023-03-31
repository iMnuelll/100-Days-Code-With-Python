'''
- Operasi komparasi / perbandingan
- Setiap hasil dari operasi komparasi adalah Boolean
- Tanda / Operasi >,<,>=,<=,==,!= dapat bekerja pada syntax literal :
    a == 4 -> a(variabel) memiliki nilai yang berarti akan tersimpan dimemori komputer. 4 adalah literal
- Operasi is dan is not tidak akan bekerja pada syntax literal. IS dan is not berfungsi untuk membandingkan Variabel atau Objek : 
    Contoh benar : a is b
    Contoh salah : a is 4
- Jika isi dari dua / lebih variabel yang berbeda sama, maka Python akan menyimpannya dimemori yang sama -> line 64 - 92
'''


a = 4
b = 2

print("LEBIH BESAR DARI (>)")
hasil = a > 3
print(f"{a} > {3} = {hasil}")
hasil = b > 3
print(f"{b} > {3} = {hasil}")
hasil = a > b
print(f"{a} > {b} = {hasil}\n")

print("LEBIH KECIL DARI (<)")
hasil = a < 3
print(f"{a} < {3} = {hasil}")
hasil = b < 3
print(f"{b} < {3} = {hasil}")
hasil = a < b
print(f"{a} < {b} = {hasil}\n")

print("LEBIH DARI / SAMA DENGAN (>=)")
hasil = a >= 3
print(f"{a} >= {3} = {hasil}")
hasil = b >= 3
print(f"{b} >= {3} = {hasil}")
hasil = a >= b
print(f"{a} >= {b} = {hasil}\n")

print("KURANG DARI / SAMA DENGAN (<=)")
hasil = a <= 3
print(f"{a} <= {3} = {hasil}")
hasil = b <= 3
print(f"{b} <= {3} = {hasil}")
hasil = a <= b
print(f"{a} <= {b} = {hasil}\n")

print("SAMA DENGAN (==)")
hasil = a == 3
print(f"{a} == {3} = {hasil}")
hasil = b == 3
print(f"{b} == {3} = {hasil}")
hasil = a == b
print(f"{a} == {b} = {hasil}\n")

print("TIDAK SAMA DENGAN (!=)")
hasil = a != 3
print(f"{a} != {3} = {hasil}")
hasil = b != 3
print(f"{b} != {3} = {hasil}")
hasil = a != b
print(f"{a} != {b} = {hasil}\n")

print("OBJECT IDENTITY is")
x = 5
y = 5
hasil = x is y
print(f"Nilai x = {x}, id = {hex(id(x))}")
print(f"Nilai y = {y}, id = {hex(id(y))}")
print(f"x is y = {hasil}")

x = 5
y = 6
hasil = x is y
print(f"Nilai x = {x}, id = {hex(id(x))}")
print(f"Nilai y = {y}, id = {hex(id(y))}")
print(f"x is y = {hasil}\n")

print("OBJECT IDENTITY is not")
x = 5
y = 5
hasil = x is not y
print(f"Nilai x = {x}, id = {hex(id(x))}")
print(f"Nilai y = {y}, id = {hex(id(y))}")
print(f"x is not y = {hasil}")

x = 5
y = 6
hasil = x is not y
print(f"Nilai x = {x}, id = {hex(id(x))}")
print(f"Nilai y = {y}, id = {hex(id(y))}")
print(f"x is not y = {hasil}")