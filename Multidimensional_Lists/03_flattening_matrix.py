rows = int(input())

flattened_matrix = []
matrix = []
for _ in range(rows):
    row_list = [int(x) for x in input().split(', ')]
    matrix.append(row_list)

flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)