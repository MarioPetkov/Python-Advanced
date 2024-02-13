from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption = deque(int(x) for x in input().split())
amount_fuel_needed = deque(int(x) for x in input().split())

reached_altitude = 0
while True:
    if not initial_fuel:
        break
    current_fuel = initial_fuel.pop()
    current_fuel -= additional_consumption.popleft()
    needed_fuel_to_reach_altitude = amount_fuel_needed.popleft()

    if current_fuel >= needed_fuel_to_reach_altitude:
        reached_altitude += 1
        print(f"John has reached: Altitude {reached_altitude}")

    else:
        print(f"John did not reach: Altitude {reached_altitude + 1}")
        break
if reached_altitude == 4:
    print(f"John has reached all the altitudes and managed to reach the top!")
elif reached_altitude > 0:
    print("John failed to reach the top. \nReached altitudes:", end = ' ')
    for i in range(1, reached_altitude + 1):
        if i < reached_altitude:
            print(f"Altitude {i},", end=" ")
        else:
            print(f"Altitude {i}")
else:
    print("John failed to reach the top. \n John didn't reach any altitude.")