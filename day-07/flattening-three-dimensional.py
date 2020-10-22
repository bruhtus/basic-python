three_dimension_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = [number for row in three_dimension_list for number in row]
print(flattened_list)

flattened_list_2 = []

for row in three_dimension_list:
    for number in row:
        flattened_list_2.append(number)

print(flattened_list_2)
