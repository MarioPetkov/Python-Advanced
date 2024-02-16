def main():
    N, M = map(int, input().split())
    neighborhood = []
    
    # Find the starting position of the delivery boy
    starting_position = None
    for row_index in range(N):
        data = list(input())
        if 'B' in data:
            current_col = data.index('B')
            starting_position = [row_index, current_col]
        neighborhood.append(data)

    if starting_position is None:
        print("Starting position 'B' not found.")
        return

    current_position = starting_position.copy()

    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    while True:
        command = input()
        if command not in directions:
            break

        next_row = current_position[0] + directions[command][0]
        next_col = current_position[1] + directions[command][1]

        # Check if the next position is within bounds
        if not (0 <= next_row < N and 0 <= next_col < M):
            print("The delivery is late. Order is canceled.")
            break

        # Check if the next position is an obstacle
        if neighborhood[next_row][next_col] == '*':
            continue

        # Move to the next position
        neighborhood[current_position[0]][current_position[1]] = '.'
        current_position = [next_row, next_col]

        # Check if the next position is an address
        if neighborhood[next_row][next_col] == 'A':
            neighborhood[next_row][next_col] = 'P'
            print("Pizza is delivered on time! Next order...")
            break

        # Check if the next position is the pizza restaurant
        if neighborhood[next_row][next_col] == 'P':
            neighborhood[next_row][next_col] = 'R'
            print("Pizza is collected. 10 minutes for delivery.")

    # Print the final state of the matrix
    for row in neighborhood:
        print("".join(row))

if __name__ == "__main__":
    main()
