# ---------------------Hangman-------------------------
'''Hangman source code file'''

import os
import random as rand
import ASCII_art as h_art
import word_list as word_list

# Printing Hangman ASCII art
print(h_art.hangman_ascii)

rand_word = rand.choice(word_list.hang_list())

# Calculating length of the random word chosen:
word_len = len(rand_word)

word_space = ""
upd_word_space = ""
already_guessed = []


#Putting in "_" (blanks) in place of the word:
for i in range(0, word_len):
    if not i == word_len:
        word_space += "_"

upd_word_space = list(word_space)

# Calculating length of the hangman_art list:
art_list_len = len(h_art.stages())

#Loop control variables:
i, j = 0, 0

print("Guess the letters: ")

# Core Hangman Logic:
while i < word_len and j < art_list_len:
    print ("Guess: ", " ".join(upd_word_space))
    inp = input().lower()
    flag = 0

    
    # Clearing the screen for UX:
    os.system('cls')

    if inp in already_guessed:
        print("Already guessed!")
        continue

    if inp == rand_word:
        i = word_len
        break
    
    for k in range(0, word_len):
        if rand_word[k] == inp:
            upd_word_space[k] = inp
            flag = 1
    #print("".join(upd_word_space))

    if flag == 1:
        already_guessed.append(inp)
        i += 1
    else:
        already_guessed.append(inp)
        print(h_art.stages()[j])
        j += 1
# Code logic end --------------------------------------------------------------

if i == word_len:
    print("Congratulations! You guessed right: ", rand_word)

elif j == art_list_len:
    print("The word was", rand_word)
    print("You ran out of moves! Better luck next time.")