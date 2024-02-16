N, M = [int(_) for _ in input().split()]

matrix = []
position = None
collected_pizza = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row_index in range(N):
    data = list(input())

    if 'B' in data:
        current_col = data.index('B')
        starting_position = [row_index, current_col]
        current_position = starting_position.copy()
    matrix.append(data)

while True:
    direction = input()
    
    if direction not in directions:
        break 

    direction_row, direction_col = directions[direction]
    next_row_index = current_position[0] + direction_row
    next_col_index = current_position[1] + direction_col
    
    if not (0 <= next_row_index < N and 0 <= next_col_index < M):
        print("The delivery is late. Order is canceled.")
        matrix[starting_position[0]][starting_position[1]] = ' '
        break
    
    next_movement = matrix[next_row_index][next_col_index]

    if next_movement == '*':
        continue

    current_position = [next_row_index, next_col_index]

    if next_movement == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[next_row_index][next_col_index] = 'R'
        collected_pizza = True
    
    elif next_movement == 'A':
        if collected_pizza:
            print("Pizza is delivered on time! Next order...")
            matrix[next_row_index][next_col_index] = 'P'
            break

    elif next_movement == '-':
        matrix[next_row_index][next_col_index] = '.'

    for row in matrix:
        print(f"{''.join(row)}")
    
for row in matrix:
    print(f"{''.join(row)}")
