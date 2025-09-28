# Definisi tuple
number_tuple = (1, 2, 3, 4, 5)
print(f"Tuple awal: {number_tuple}")

# Mengakses item dalam tuple
print(f"Elemen pertama: {number_tuple[0]}")
print(f"Slice dari indeks 1 hingga 3: {number_tuple[1:4]}")

# Menambahkan tuple dengan tuple lain
new_tuple = number_tuple + (6, 7, 8)
print(f"Tuple setelah ditambahkan elemen baru: {new_tuple}")

# Mengulang tuple
repeated_tuple = number_tuple * 2
print(f"Tuple setelah dikalikan 2: {repeated_tuple}")

# Menampilkan informasi tambahan tentang tuple
print(f"Panjang tuple: {len(number_tuple)}")
print(f"Nilai minimum dalam tuple: {min(number_tuple)}")
print(f"Nilai maksimum dalam tuple: {max(number_tuple)}")

# Contoh tuple dengan tipe data berbeda
mixed_tuple = (1, "Python", 3.14, True)
print(f"Tuple dengan berbagai tipe data: {mixed_tuple}")

# Looping dalam tuple
print("Looping melalui tuple:")
for item in number_tuple:
    print(f"- {item}")

