unique_elements = set()

for _ in range(int(input())):
    chemical_compounds = input().split()
    for el in chemical_compounds:
        unique_elements.add(el)
print(*unique_elements, sep = '\n')