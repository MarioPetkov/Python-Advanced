guests_num = int(input())
codes = set()

for _ in range(guests_num):
    code = input()
    codes.add(code)

code = input()
while code != 'END':
    if code in codes:
        codes.remove(code)
    code = input()

print(len(codes))
for code in sorted(codes):
    print(code)