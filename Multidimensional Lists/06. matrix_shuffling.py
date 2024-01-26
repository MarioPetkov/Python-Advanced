def check_indices_valid(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_columns)

def swap_elements(command, indices):
    if len(indices) == 4 and check_indices_valid(indices) and command == "swap":
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1] 

        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
rows, columns = (int(x) for x in input().split())

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

valid_rows = range(rows)
valid_columns = range(columns)

while True:
    function, *coords = [int(x) if x.isdigit() else x for x in input().split()]

    if function == 'END':
        break
    
    swap_elements(function, coords)
