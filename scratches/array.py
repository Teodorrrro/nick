array = [1, [3, 1, 'asd'], {'hello': 132}]

print(array)
print(array[0])
print(array[1][1])
print(array[2]['hello'])


arr = [1, 2, 4, 1, 2, 3]

new_arr_square = []
for i in arr:
    if i != 1:
        new_arr_square.append(i**2)
print(new_arr_square)

square_arr = [i ** 2 for i in arr if i != 1]
print(square_arr)


arr3 = [2, 2, 1, 1,2, 1]

m = set(arr3)

print(m)
arr3 = list(m)
print(arr3)
