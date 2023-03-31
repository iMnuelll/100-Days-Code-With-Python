# Latihan Konversi Satuan Temperature

print("\t===PROGRAM KONVERSI TEMPERATURE ===")

celcius = float(input("Masukkan suhu dalam celcius : "))
print(f"Suhu adalah {celcius} Celcius")

# Reamur
reamur = (4/5) * celcius
print(f"Suhu dalam reamur adalah {reamur} Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print(f"Suhu dalam Fahrenheit adalah {fahrenheit} Fahrenheit")

# Kelvin
kelvin = celcius + 273
print(f"Suhu dalam kelvin adalah {kelvin} Kelvin")

# Tugas
fahrenheit_ke_kelvin = (5/9*(fahrenheit-32)) + 273
print(f"Suhu Fahrenheit ke Kelvin adalah {fahrenheit_ke_kelvin}")

kelvin_ke_fahrenheit = (9/5 * (kelvin - 273) + 32)
print(f"Suhu Kelvin ke Fahrenheit adalah {kelvin_ke_fahrenheit}")