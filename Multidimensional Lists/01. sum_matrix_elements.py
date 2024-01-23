row, col = input().split(', ')

matrix = []
total_sum = 0

for _ in range(int(row)):
    sub_matrix = [int(x) for x in input().split(', ')]
    total_sum += sum(sub_matrix)
    matrix.append(sub_matrix)
print(total_sum)
print(matrix)