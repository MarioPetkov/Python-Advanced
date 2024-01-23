matrix_rows = int(input())

even_matrix = []
for row in range(matrix_rows):
    even_row = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
    even_matrix.append(even_row)
print(even_matrix)