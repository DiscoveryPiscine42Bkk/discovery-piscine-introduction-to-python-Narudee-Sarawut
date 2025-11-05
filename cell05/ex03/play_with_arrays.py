original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
for number in original_array:
    if number > 5:
        value = number + 2
        if value not in new_array:
            new_array.append(value)
print("Original array:", original_array)
print("Processed array (values > 5, +2, no duplicates):", new_array)
