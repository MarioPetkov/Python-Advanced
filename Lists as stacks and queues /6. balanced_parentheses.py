text = input()
paren_index = []

for index in range(len(text)):
    if text[index] == "(":
        paren_index.append(index)
    elif text[index] == ")":
        start_index = paren_index.pop()
        end_index = index + 1
        print(text[start_index:end_index])