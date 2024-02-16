matrix = []

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for row in range(int(input())):
    data = list(input()) 

    if 'G' in data:
        starting_position = [row, data.index('G')]
        data[data.index('G')] = '-'
        money = 100
    matrix.append(data)


while True:
    command = input()

    if command == 'end':
        print(f"End of the game. Total amount: {money}$")
        break

    next_row = direction[command][0] + starting_position[0]
    next_col = direction[command][1] + starting_position[1]

    if matrix[next_row][next_col] == '-':
        pass

    elif matrix[next_row][next_col] == 'W':
        money += 100

    elif matrix[next_row][next_col] == 'P':
        money -= 200


    elif matrix[next_row][next_col] == 'J':
        money += 100000
        matrix[next_row][next_col] = '-'
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
        break

    matrix[next_row][next_col] = '-'
    starting_position = [next_row, next_col]

    if money <= 0 or not (0 <= next_row < len(matrix) and 0 <= next_col < (len(matrix))):
        print(f"Game over! You lost everything!")
        exit()

matrix[next_row][next_col] = 'G'
for row in matrix:
    print(f"{''.join(row)}")