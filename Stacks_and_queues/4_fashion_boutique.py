box_of_clothes = [int(x) for x in input().split()]
capacity = int(input())
counter = 1
current_capacity = capacity
while box_of_clothes:
    last_item = box_of_clothes.pop()
    if current_capacity >= last_item:
        current_capacity -= last_item
    elif current_capacity < last_item:
        counter += 1
        current_capacity = capacity
        current_capacity -= last_item
print(counter)
