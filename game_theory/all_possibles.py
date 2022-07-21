def file_to_list(filename):
    f = open(filename, 'r')
    a_list = []
    for line in f:
        stripped_line = line.strip().lower()
        a_list.append(stripped_line)
    f.close()
    return a_list

words = file_to_list('new_wordles.txt')
possibles = []

for word in words:
    if 'e' in word:
        pass
    else:
        if word[1] == 'r' and word[2] == 'a' and word[3] == 's':
            possibles.append(word)

print(possibles)