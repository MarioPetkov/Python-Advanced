from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk_cups = deque(int(x) for x in input().split(', '))

chocolate_milkshakes = 0

while chocolate_milkshakes != 5 and chocolates and milk_cups:
    chocolate = chocolates.pop()
    cup_of_milk = milk_cups.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        milk_cups.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if cup_of_milk == chocolate:
        chocolate_milkshakes += 1
    else:
        milk_cups.append(cup_of_milk)
        chocolates.append(chocolate - 5)

if chocolate_milkshakes >= 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk_cups) or 'empty'}")