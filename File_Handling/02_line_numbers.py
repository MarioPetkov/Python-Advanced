from string import punctuation

with open('File_Handling/even_lines.txt', 'r') as text_file:
    text = text_file.readlines()

output_file = open('File_Handling/output.txt', 'w')

for row in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f'Line {row + 1}: {text[row][:-1]} ({letters})({marks})\n')

output_file.close()

# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.