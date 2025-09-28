# Accessing list items
number_list = [1, 2, 3, 4, 5]
# number_list.reverse()

i=0
print(f"this is a value in list index {i} = {number_list[i]}")

i=-1
print(f"this is a value in list using index {i} = {number_list[i]}")

start_index = 1
end_index = 4
range_list = number_list[start_index : end_index]
print(f"this is a value from list in index range {start_index}-{end_index}: {range_list}")
print(f"print number with range : {number_list[1:4]}")


# Add items to list
number_list.append(6)
print(number_list)
number_list.insert(1, 10)
print(number_list)
number_list.extend([7, 8])
print(number_list)

# Remove items on list
number_list.remove(10)
print(number_list)
number_list.pop(3)
print(number_list)
number_list.clear()
print(number_list)

# Change item on list
number_list = [1, 2, 3, 4, 5, 6, 7, 7, 9]
number_list[0] = 100
print(number_list)

# Additional
print(len(number_list))
print(min(number_list))
print(sorted(number_list))
print(number_list[::2])

# List comprehension
squared = [x**2 for x in number_list]
print(squared)
