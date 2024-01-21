from collections import deque
food_qty = int(input())
queue = deque(int(x) for x in input().split())

print(max(queue))
while queue:
    if queue[0] <= food_qty:
        food_qty -= queue[0]
        queue.popleft()
    else:
        break

if queue:
    print("Orders left:", *queue, sep = ' ')
else:
    print("Orders complete")