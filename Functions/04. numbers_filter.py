def even_odd_filter(**numbers_sets):
    if "odd" in numbers_sets:   
        numbers_sets["odd"] = [int(n) for n in numbers_sets["odd"] if int(n) % 2 != 0 ]
    if "even" in numbers_sets:
        numbers_sets["even"] = [int(n) for n in numbers_sets["even"] if int(n) % 2 == 0 ]
    return dict(sorted(numbers_sets.items(), key=lambda x: -len(x[1])))



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))