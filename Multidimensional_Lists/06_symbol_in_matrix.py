row_col = int(input())

matrix = []
for _ in range(row_col):
    matrix.append(list(input()))

searched_sym = input()
for row_index in range(row_col):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_sym:
            print(f'({row_index}, {col_index})')
            exit()

print(f"{searched_sym} does not occur in the matrix")
        
# 3
# ABC
# DEF
# X!@
# !