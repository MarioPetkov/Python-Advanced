from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())
matches = 0
removed_worms = 0

while worms and holes:

    if worms[-1] == holes[0]:
        worms.pop()
        holes.popleft()
        matches += 1
    
    else:
        holes.popleft()
        worms[-1] -= 3

        if worms[-1] <= 0:
            worms.pop()
            removed_worms += 1
    
if matches > 0:
    print(f'Matches: {matches}')
else:
    print('There are no matches.')

if not worms and removed_worms > 0:
    print("Worms left: none")
elif not worms and removed_worms == 0:
    print("Every worm found a suitable hole!")
else:
    worm_str = ", ".join(map(str, worms))
    print(f"Worms left: {worm_str}")

if not holes:
    print("Holes left: none")
else:
    holes_str = ", ".join(map(str, holes))
    print(f"Holes left: {holes_str}")
    
