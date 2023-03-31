"""
- Membuat gabungan area rentang dari angka :
    ++++3-------10++++
"""

print("GABUNGAN")
askUser = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10 : "))

# Memeriksa angka kurang dari 3
KurangDari3 = askUser < 3
print(f"Kurang dari 3 = {KurangDari3}")

# Memeriksa angka lebih dari 10
LebihDari10 = askUser > 10
print(f"Lebih dari 10 = {LebihDari10}")

# Memeriksa angka apakah kurang dari 3 atau lebih dari 10
gabungan = KurangDari3 or LebihDari10
print(f"Apakah angka yang dimasukkan memenuhi klasifikasi : {gabungan}")

"""
- Membuat irisan area rentang dari angka :
    ----3+++++++10----
"""
print("\nIRISAN")
askUser = float(input("Masukkan angka yang bernilai lebih dari 3 dan kurang dari 10 : "))

# Memeriksa angka lebih dari 3
LebihDari3 = askUser > 3
print(f"Lebih dari 3 = {LebihDari3}")

# Memeriksa angka kurang dari 10
KurangDari10 = askUser < 10
print(f"Kurang dari 10 = {KurangDari10}")

# Memeriksa angka apakah lebih dari 3 dan kurang dari 10 (Melakukan irisan)
irisan = LebihDari3 and KurangDari10
print(f"Angka yang anda masukkan memenuhi klasifikasi : {irisan}")

