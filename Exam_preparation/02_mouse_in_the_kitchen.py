R, C = [int(x) for x in input().split(',')]
matrix = []
cheese_count = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row_index in range(R):
    data = list(input())

    if 'C' in data:
        cheese_count += data.count('C')

    if 'M' in data:
        current_col = data.index('M')
        current_position = [row_index, current_col]
        data[current_col] = '*'
        
    matrix.append(data)

while True:
    command = input()

    if command == 'danger':
        print("Mouse will come back later!")
        break

    row_index = directions[command][0] + current_position[0]
    col_index = directions[command][1] + current_position[1]
    
    if not (0 <= row_index < R and 0 <= col_index < C):
        print("No more cheese for tonight!")
        break

    symbol = matrix[row_index][col_index]

    if symbol == 'C':
        matrix[row_index][col_index] = '*'
        cheese_count -= 1
        current_position = [row_index, col_index]


        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif symbol == 'T':
        current_position = [row_index, col_index]
        print("Mouse is trapped!")
        break

    elif symbol == '@':
        continue
    
    elif symbol == '*':
        current_position = [row_index, col_index]


matrix[current_position[0]][current_position[1]] = 'M'

for row in matrix:
    print(f"{''.join(row)}")

