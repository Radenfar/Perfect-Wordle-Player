f = open('list_of_wordles.txt', 'r')
all_answers = []
for line in f:
    stripped_line = (line.strip()).lower()
    all_answers.append(stripped_line)
f.close()

def find_possibles(letters, all_answers):
    possibilities = []
    for answer in all_answers:
        test  = all(x in answer for x in letters)
        if test == True:
            possibilities.append(answer)
    return possibilities

def exclude_from_position(letter, index, possibilities):
    new_possibilities = []
    for answer in possibilities:
        if answer[index] == letter:
            pass
        else:
            new_possibilities.append(answer)
    return new_possibilities

def total_exclusion(letter, possibilities):
    new_possibilities = []
    for answer in possibilities:
        if letter in answer:
            pass
        else:
            new_possibilities.append(answer)
    return new_possibilities

def include_from_position(letter, index, possibilities):
    new_possibilities = []
    for answer in possibilities:
        if answer[index] == letter:
            new_possibilities.append(answer)
        else:
            pass
    return new_possibilities

letters = []
#main routine
while True:
    letter_input = input("Enter a letter, enter nothing to stop -: ")
    if letter_input == '':
        break
    else:
        letters.append(letter_input)

possibilities = find_possibles(letters, all_answers)
possibilities = include_from_position('u', 1, possibilities)
possibilities = include_from_position('r', 4, possibilities)
possibilities = total_exclusion('t', possibilities)
possibilities = total_exclusion('a', possibilities)
possibilities = total_exclusion('i', possibilities)
possibilities = total_exclusion('l', possibilities)
possibilities = total_exclusion('q', possibilities)
print(possibilities)    
