stack = []
n_queries = int(input())
for _ in range(n_queries):
    query = input().split(' ')
    if query[0] == '1':
        number = int(query[1])
        stack.append(number)
    if query[0] == '2':
        if stack:
            stack.pop()
    if query[0] == '3':
        if stack:
            print(max(stack))
    if query[0] == '4':
        if stack:
            print(min(stack))
while len(stack) > 1:
    print(stack.pop(), end = ', ')
print(stack.pop(), end = ' ')