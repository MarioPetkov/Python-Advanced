import sys
rows, columns = map(int, input().split(', '))

matrix = []
biggest_sum = -sys.maxsize
sub_matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        current_element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index + 1]
        lower_element = matrix[row_index + 1][column_index]
        diagonal_element = matrix[row_index + 1][column_index + 1]

        current_sum = current_element + next_element + diagonal_element + lower_element
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            sub_matrix = [[current_element, next_element], [lower_element, diagonal_element]]
print(*sub_matrix[0])
print(*sub_matrix[1])
print(biggest_sum)
