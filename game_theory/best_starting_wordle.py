def file_to_list(filename):
    f = open(filename, 'r')
    a_list = []
    for line in f:
        stripped_line = line.strip().lower()
        a_list.append(stripped_line)
    f.close()
    return a_list

def list_to_file(a_list, filename):
    f = open(filename, 'w')
    for item in a_list:
        f.write("%s\n" % item)
    print('Array Write Complete.')

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

def update_scores():
    #function to use if the list of wordles ever gets updated again
    wordle_list = file_to_list('new_wordles.txt')
    score_list = []
    for word in wordle_list:
        score_list.append(get_score_word(word, wordle_list))
    list_to_file(score_list, 'wordle_scores.txt')

wordle_list = file_to_list('new_wordles.txt')
score_string_list = file_to_list('wordle_scores.txt')
score_list = ([float(x) for x in score_string_list])
print(max(score_list))
index_of_highest = score_list.index(max(score_list))
print(wordle_list[index_of_highest])