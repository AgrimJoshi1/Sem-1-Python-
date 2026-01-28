'''take input of pixels 3rows, give average brightness and max brightness in which row'''
matrix_pixel = []
for i in range (3):
    row = []
    for j in range(3):
        element = int(input(f"Enter element at ({i+1}, {j+1}): "))
        row.append(element)
    matrix_pixel.append(row)

row_sums = [sum(row) for row in matrix_pixel]
total_sum = sum(row_sums)
num_pixels = sum(len(row) for row in matrix_pixel)
avg_brightness = total_sum / num_pixels
brightest_row = row_sums.index(max(row_sums)) + 1 


print("Average brightness:", avg_brightness)
print("Brightest row:", brightest_row)