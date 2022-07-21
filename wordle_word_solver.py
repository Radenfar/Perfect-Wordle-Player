f = open('list_of_wordles.txt', 'r')
all_answers = []
for line in f:
    stripped_line = (line.strip()).lower()
    all_answers.append(stripped_line)
f.close()

def remove_dupes(a_list):
  return list(dict.fromkeys(a_list))

def dict_to_str(word):
    word = ''.join(str(x) for x in word.values())
    return word

def not_in_x(keep_list, remove_list):
    for i in keep_list[:]:
        if i in remove_list:
            remove_list.remove(i)
    return remove_list

def find_possibles(word, all_answers):
    values_list = list(word.values())
    non_words = []
    for i in range(5):
        if values_list[i] == "_":
            pass
        else:
            cur_char = values_list[i]
            for answer in all_answers:
                if answer[i] != cur_char:
                    non_words.append(answer)
    possibilities = not_in_x(non_words, all_answers)
    return possibilities

word = {1: '_', 2: '_', 3: '_', 4: '_', 5: '_'}

#main routine
while True:
    letter_input = input("Enter a letter -: ")
    number_input = int(input("Enter the number place its in 1-5 -: "))
    word[number_input] = letter_input
    print(dict_to_str(word))
    print('-'*20)
    print('Possibilities:')
    print('-'*20)
    cur_possibilities = find_possibles(word, all_answers)
    print(cur_possibilities)
