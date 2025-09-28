# Pembuatan dictionary
person_info = {'name': 'Alice', 'age': 25, 'job': 'Engineer'}

# Accessing dictionary
print(person_info['name'])
print(person_info.get('age'))

# Update dictionary menggunakan update()
person_info.update({'age': 26, 'city': 'New York'})
print(person_info)

# Hapus key dan value dalam dictionary
person_info.pop('job', None)
person_info.pop('city', None)
print(person_info)

# Iterasi dalam dictgionary
for items in person_info.items():
    print(f"{items}")
