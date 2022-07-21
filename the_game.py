import random

win = False

f = open('list_of_wordles.txt', 'r')
all_answers = []
for line in f:
    stripped_line = (line.strip()).lower()
    all_answers.append(stripped_line)
f.close()

answer = random.choice(all_answers)
answer_list = list(answer)

wordle_guesses = [
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"]
]

wordle_reveal = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

def wordle_print(wordle):
    game = ""
    for row in wordle:
        row_print = ""
        for char in row:
            row_print += char + " "
        game += row_print + "\n"
    return game[:-1]

def info(wordle_guesses, wordle_reveal):
    printer = (" "*20)
    print(printer)
    print(wordle_print(wordle_guesses))
    print(printer)
    print(wordle_print(wordle_reveal))
    return print(printer)

#main routine
print("-"*20)
print("Welcome to Adam's Wordle in Python")
print("Without the usual coloured letters, there are a new set of rules:")
print("You will be shown two tables.")
print("The top one shows your guesses, the bottom reveals the hints.")
print("A 0 means the letter is totally invalid to the word.")
print("A 1 means the letter is in the word but not where you put it.")
print("A 2 means you have placed that letter perfectly!")
print("Good luck!")
print("-"*20)
info(wordle_guesses, wordle_reveal)
for x in range(6):
    print("Guess " + str(x+1) + ":")
    word_input = input("Enter a 5 letter word -: ").lower()
    if word_input == answer:
        win = True
        break
    word_x_list = list(word_input)
    wordle_guesses[x] = word_x_list
    for i in range(5):
        cur_guess = wordle_guesses[x][i]
        cur_answer_char = answer_list[i]
        if cur_guess == cur_answer_char:
            wordle_reveal[x][i] = "2"
        elif cur_guess in answer_list:
            wordle_reveal[x][i] = "1"
    
    info(wordle_guesses, wordle_reveal)
    print("-"*20)

if win == True:
    print("Congrats! You won!")
else:
    print("You're shit mate")
    print("The answer was clearly " + answer + ".")
