# Membuat set awal
number_set = {1, 2, 3, 4, 5}
print(f"Set awal: {number_set}")

# Menambahkan satu elemen kedalam set
number_set.add(6)
print(f"Set setelah menambahkan angka 6: {number_set}")

# Menambahkan beberapa elemen dengann update()
number_set.update([7, 7, 8, 9])
print(f"Set setelah menambahkan beberapa angka: {number_set}")

# Menghapus elemen 5 dari set
try:
    number_set.remove(5)
    print(f"Set setelah menghapus angka 5: {number_set}")
except Exception as e:
    raise Exception(f"Nilai tidak bisa dihapus karena nilai {e} tidak ditemukan")

# Menggunakan discard() untuk menghapus elemen

try:
    number_set.discard(100)
    print(f"Set setelah mencoba menghapus angka 9 (dengan discard): {number_set}")
except Exception as e:
    raise Exception(f"Nilai tidak bisa dihapus karena nilai {e} tidak ditemukan")

# Menghapus elemen secara acak dengan pop()
if number_set:
    popped_value = number_set.pop()
    print(f"Elemen yang dihapus dengan pop(): {popped_value}")
    print(f"Set setelah pop(): {number_set}")
else:
    print("Set kosong, tidak bisa pop()")

# Menghapus semua elemen dari set
number_set.clear()
print(f"Set setelah di-clear(): {number_set}")

# Operasi set dasar
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Gabungan set1 dan set2 (gabungan): {set1 | set2}")
print(f"Irisan set1 dan set2 (irisan): {set1 & set2}")
print(f"Selisih set1 - set2 (difference): {set2 - set1}")
print(f"Selisih simetris set1 ^ set2 (symmetric difference): {set1 ^ set2}")

# Membuat set dengan comprehension untuk angka genap
even_numbers = {x for x in range(10) if x % 2 == 0}
print(f"Set angka genap dari 0 hingga 9: {even_numbers}")
