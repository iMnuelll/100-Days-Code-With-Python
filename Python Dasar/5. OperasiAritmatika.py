a = 10
b = 3

print("\t=== OPERASI ARITMATIKA ===")
# Tambah
hasil = a+b
print(a, "+", b, "=", hasil)

# Pengurangan
hasil = a-b
print(a, "", b, "=", hasil)

# Kali 
hasil = a*b
print(a, "*", b, "=", hasil)

# Pembagian
hasil = a/b
print(a, "/", b, "=", hasil)

# Eksponen (Pangkat)
hasil = a**b
print(a, "**", b, "=", hasil)

# Modulo (Hasil bagi)
hasil = a%b
print(a, "%", b, "=", hasil)

# Floor division (Kebalikan modulo) -> Hasil dari float diturunkan ke bawah
hasil = a//b
print(a, "//", b, "=", hasil)

# NOTE : PRIORITAS OPERASI -> (), eksponen, perkalian-bagi-modulo-floor division, tambah-kurang
# PENJELASAN LEBIH LENGKAP : https://www.youtube.com/watch?v=RoDGGTWbKK4&list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1&index=10