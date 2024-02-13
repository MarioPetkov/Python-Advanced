def is_digit(current_row, current_col, matrix_size):

    row = (current_row + matrix_size) % matrix_size
    col = (current_col + matrix_size) % matrix_size
        
    return row, col

fishing_area = int(input())

matrix = []
fisher_pos = []
successful_season = False

quantity = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(fishing_area):
    row_data = [el for el in input()]
    matrix.append(row_data)

    if 'S' in row_data: 
        c = row_data.index('S')
        fisher_pos = [r,c]   

        matrix[r][c] = '-'  

while True:
    command = input()

    if command == 'collect the nets':
        break

    row = fisher_pos[0] + directions[command][0]
    col = fisher_pos[1] + directions[command][1]

    row, col = is_digit(row, col, fishing_area)
    fisher_pos = [row, col]

    symbol = matrix[row][col]

    if symbol.isdigit():
        quantity += int(symbol)
        matrix[row][col] = '-' 

    elif symbol == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{fisher_pos[0]},{fisher_pos[1]}]")
        exit()

matrix[row][col] = 'S'  

if quantity >= 20:
    successful_season = True

if successful_season:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! \nYou need {20 - quantity} tons of fish more.")

if quantity > 0:
    print(f'Amount of fish caught: {quantity} tons.')

for row in matrix:
    print(''.join(row))
