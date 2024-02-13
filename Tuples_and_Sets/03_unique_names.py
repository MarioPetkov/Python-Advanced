names_num = int(input())
unique_names = []

for _ in range(names_num):
    name = input()
    if name not in unique_names:
        unique_names.append(name)
for name in unique_names:
    print(name)