from collections import deque

monsters_armor = deque(int(_) for _ in input().split(','))
soldiers_strength = [int(_) for _ in input().split(',')]

killed_monsters = 0

while monsters_armor and soldiers_strength:

    armor_value = monsters_armor[0]
    strength_value = soldiers_strength[-1]

    if armor_value <= strength_value:   
        monsters_armor.popleft()
        soldiers_strength[-1] -= armor_value

        if len(soldiers_strength) > 1:
            soldiers_strength[-2] += soldiers_strength[-1]

        soldiers_strength.pop()
        killed_monsters += 1

    else: 
        monsters_armor[0] -= soldiers_strength.pop()
        monsters_armor.append(monsters_armor.popleft())

if not monsters_armor:
    print("All monsters have been killed!")

elif not soldiers_strength:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
