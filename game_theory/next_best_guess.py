def file_to_list(filename):
    f = open(filename, 'r')
    a_list = []
    for line in f:
        stripped_line = line.strip().lower()
        a_list.append(stripped_line)
    f.close()
    return a_list

def get_score_letter(letter, position, wordle_list):
    #letter in that position -> += 0.002
    #letter somewhere in that word -> += 0.001
    score = 0
    for word in wordle_list:
        if word[position] == letter:
            score += 0.002
        elif letter in word:
            score += 0.001
        else:
            pass
    return score

def get_score_word(word, wordle_list):
    score = 0
    for i in range(5):
        score += get_score_letter(word[i], i, wordle_list)
    return score

def barred_check(barred, previous_possibilities):
    new_list = []
    for word in previous_possibilities:
        if any(char in word for char in barred):
            pass
        else:
            new_list.append(word)
    return new_list

def must_include_check(must_include, previous_possibilities):
    new_list = []
    for key in must_include:
        cur_letter = must_include[key]
        for word in previous_possibilities:
            if word[key] == cur_letter:
                pass
            elif cur_letter not in word:
                pass
            elif word in new_list:
                pass
            else:
                new_list.append(word)
    return new_list

def must_have_check(must_have, previous_possibilities):
    new_list = []
    for word in previous_possibilities:
        check = True
        for key in must_have:
            cur_letter = must_have[key]
            if word[key] == must_have[key]:
                check = True
            else:
                check = False
        if check == True and word not in new_list:
            new_list.append(word)
    return new_list

def do_round(binary_string, possibilities, wordle_list):
    previous_guess = possibilities[1]
    previous_possibilities = possibilities[0]
    must_have = {} #position it must be, letter
    must_include = {} #position it CANT be, letter
    barred = [] #any letter that is not in the string
    for i in range(len(binary_string)):
        if binary_string[i] == '0':
            barred.append(previous_guess[i])
        elif binary_string[i] == '1':
            must_include[i] = previous_guess[i]
        else:
            must_have[i] = previous_guess[i]
    new_possibilities = barred_check(barred, previous_possibilities)
    new_possibilities = must_include_check(must_include, new_possibilities)
    new_possibilities = must_have_check(must_have, new_possibilities)
    new_score_list = []
    for word in new_possibilities:
        new_score_list.append(get_score_word(word, new_possibilities))
    index_best = new_score_list.index(max(new_score_list))
    new_guess = new_possibilities[index_best]
    print("Best guess: '%s'" %new_guess)
    print("Score:", max(new_score_list))
    return [new_possibilities, new_guess]

#initialisation
#BOT RELIES ON UNDERSTANDING OF POSSIBILITIES. This is a nested array with [remaning possible words, previous guess]
wordle_list = file_to_list('new_wordles.txt')
score_string_list = file_to_list('wordle_scores.txt')
score_list = ([float(x) for x in score_string_list])
possibilities_nest = file_to_list('new_wordles.txt')
possibilities = [possibilities_nest, 'erase']

index_of_highest = score_list.index(max(score_list))
starting_word = (wordle_list[index_of_highest])

print('Perfect Wordle Player')
print('---------------------')
print('0 = Letter not in word')
print('1 = Letter in word but not that position')
print('2 = Letter in that position')
print('At the end of each round, enter a length-5 binary string to represent the outcome of the last round.')
print("Example: '01110'")
print('---------------------')
print('Round 1')
print("Best starting guess: '%s'" %starting_word)
print("Score:", max(score_list))
print('-'*5)
round_num = 2
for i in range(5):
    print('Round', round_num)
    binary_string = input("Enter binary string from last round -: ")
    possibilities = do_round(binary_string, possibilities, wordle_list)
    print('-'*5)
    round_num += 1