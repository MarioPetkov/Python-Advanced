N, M = [int(_) for _ in input().split()]

matrix = []
position = None

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
        position = [row_index, current_col]
    matrix.append(data)

while True:
    command = input()

    if is_in_matrix():
        pass
    for row in range(N):
        
        for col in range(M):

            next_row_index = row + 
    

# 'B' - Represents the starting position of the delivery boy.
# 'A' - Represents an address where a pizza needs to be delivered.
# '*' - Represents an obstacle or an area where the delivery boy cannot drive.
# 'P' - Represents the pizza restaurant.
# '-' – Represents the road, the delivery boy can drive over it.