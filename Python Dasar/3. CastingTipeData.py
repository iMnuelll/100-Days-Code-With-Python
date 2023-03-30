# Merubah tipe data

# Integer
print("\t=== INTEGER ===")
data_int = 9
print("data = ", data_int, "type = ",type(data_int))

data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int) # -> Akan false jika nilai int = 0

print("data = ", data_float, "type = ",type(data_float))
print("data = ", data_string, "type = ",type(data_string))
print("data = ", data_bool, "type = ",type(data_bool))

# Float
print("\t=== FLOAT ====")
data_float = 9.5
print("data = ", data_float, "type = ",type(data_float))

data_int = int(data_float) # -> Akan dibulatkan ke bawah
data_string = str(data_float)
data_bool = bool(data_float) # -> Akan false jika nilai int / float = 0

print("data = ", data_int, "type = ",type(data_int))
print("data = ", data_string, "type = ",type(data_string))
print("data = ", data_bool, "type = ",type(data_bool))

# Boolean
print("\t=== BOOLEAN ====")
data_bool = True
print("data = ", data_bool, "type = ",type(data_bool))

data_int = int(data_bool)
data_string = str(data_bool)
data_float = float(data_bool) # -> Akan false jika nilai int = 0

print("data = ", data_int, "type = ",type(data_int))
print("data = ", data_string, "type = ",type(data_string))
print("data = ", data_float, "type = ",type(data_float))

# String
print("\t=== String ====")
data_str = ("10")
print("data = ", data_str, "type = ",type(data_str))

data_int = int(data_str) # -> String harus angka, jika tidak akan error
data_bool = bool(data_str) # -> String harus angka, jika tidak akan error
data_float = float(data_str) # -> Akan false jika string kosong

print("data = ", data_int, "type = ",type(data_int))
print("data = ", data_bool, "type = ",type(data_bool))
print("data = ", data_float, "type = ",type(data_float))