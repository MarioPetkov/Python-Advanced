cars_num = int(input())
parking = []


for _ in range(cars_num):
    direction, car_number = input().split(', ')
    if direction == 'IN' and car_number not in parking:
        parking.append(car_number)
    elif direction == 'OUT' and car_number in parking:
        parking.remove(car_number)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")