rows_num = int(input())

matrix = []
diagonal_sum = 0
for _ in range(rows_num):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for index in range(rows_num):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)