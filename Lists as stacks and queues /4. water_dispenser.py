from collections import deque
water_qty = int(input())
queue = deque()
name = input()

while name != 'Start':
    queue.append(name)
    name = input()


while True:
    command = input().split(' ')
    if command[0] == 'End':
        break
    elif command[0] == "refill":
        water_qty += int(command[1])
    else:
        liters = int(command[0])
        if liters <= water_qty:
            print(f"{queue.popleft()} got water")
            water_qty -= liters
        else:
            print(f"{queue.popleft()} must wait")
print(f"{water_qty} liters left")