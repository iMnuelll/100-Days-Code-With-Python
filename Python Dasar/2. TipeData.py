# Tipe Data : Angka Satuan (Integer)
data_integer = 1
print("Data : ", data_integer, ", bertipe : ", type(data_integer))

# Tipe Data : Float
data_float = 1.5
print("Data : ", data_float, ", bertipe : ", type(data_float))

# Tipe Data : String (Kumpulan karakter)
data_string = "IDontKnow"
print("Data : ", data_string, ", bertipe : ", type(data_string))

# Tipe Data : Boolean (True / False)
data_boolean = True
print("Data : ", data_boolean, ", bertipe : ", type(data_boolean))

# Tipe data khusus
# 1. Bilangan kompleks -> complex(real, imaginary)
data_complex = complex(5, 6)
print("Data : ", data_complex, ", bertipe : ", type(data_complex))

# 2. Tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("Data : ", data_c_double, ", bertipe : ", type(data_c_double))