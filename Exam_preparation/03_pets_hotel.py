def accommodate_new_pets(hotel_capacity: int, maximum_weight_per_pet: float, *animals):
    hotel_pets = {}
    result = []

    for pet_type, pet_weight in animals:

        if hotel_capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break

        elif pet_weight > maximum_weight_per_pet:
            continue

        elif pet_weight <= maximum_weight_per_pet:

            if pet_type not in hotel_pets:
                hotel_pets[pet_type] = 0
                
            hotel_pets[pet_type] += 1
            hotel_capacity -= 1
    else:
        result.append(f'All pets are accommodated! Available capacity: {hotel_capacity}.')

    result.append('Accommodated pets:')
    [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(hotel_pets.items())]
    return '\n'.join(result)

print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))