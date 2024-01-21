from collections import deque
names = deque(input().split(' '))
n_toss = int(input())

while len(names) > 1:
    names.rotate(-n_toss)
    print(f'Removed {names.pop()}')
print(f'Last is {names.pop()}')