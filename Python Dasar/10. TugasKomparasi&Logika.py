"""
Soal 1 -> -----0+++++5------8+++++11-----
Soal 2 -> +++++0-----5++++++8-----11+++++
"""

# Soal 1
print("SOAL 1")
askUser = float(input("""Masukkan angka dengan spesifikasi berikut : 
1. Lebih dari 0 atau  kurang dari 5
2. Lebih dari 8 atau kurang dari 11\n: """))
lebihDari0 = askUser > 0
kurangDari5 = askUser < 5
gabungan1 = lebihDari0 and kurangDari5
print(f"Hasil gabungan 1 : {gabungan1}")

lebihDari8 = askUser > 8
kurangDari11 = askUser < 11
gabungan2 = lebihDari8 and kurangDari11
print(f"Hasil gabungan 2 : {gabungan2}")

print(f"Hasil gabungan 1 dan gabungan 2 : {gabungan1 or gabungan2}")

# Soal 2
print("\nSOAL 2")
askUser = float(input("""Masukkan angka dengan spesifikasi berikut : 
1. Kurang dari 0
2. Lebih dari 5 atau kurang dari 8
3. Lebih dari 11\n: """))
kurangDari0 = askUser < 0
print(f"Kurang dari 0 : {kurangDari0}")

lebihdari5 = askUser > 5
kurangDari8 = askUser < 8
gabungan1 = lebihdari5 and kurangDari8
print(f"Angka lebih dari 5 dan kurang dari 8 : {gabungan1}")

lebihDari11 = askUser > 11
print(f"Angka lebih dari 11 : {lebihDari11}")

gabungan2 = kurangDari0 or gabungan1 or lebihDari11
print(f"Angka yang anda masukkan sudah sesuai dengan speifikasi : {gabungan2}")