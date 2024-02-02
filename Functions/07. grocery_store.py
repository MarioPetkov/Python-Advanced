def grocery_store(**products):
    result = ""
    sorted_result = sorted(
        products.items(),
        key = lambda kvp: (-kvp[1], (-len(kvp[0])), (kvp[0])))
    
    for product, quantity in sorted_result:
        result += f'{product}: {quantity}\n'
    return result

print(grocery_store(
    bread=5,
    pasta=12, 
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))