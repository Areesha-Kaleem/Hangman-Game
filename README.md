# Hangman-Game
 This code is a basic hangman game with multiple levels. It uses the random module and the art module to display fancy text. The player is welcomed, prompted to guess letters, and their progress is displayed. The score is adjusted based on correct or incorrect guesses, and the game ends with a win message and total score.

1. Imports and Setup:
import random
from art import *

import random: This imports the random module, which allows the program to generate random choices.
from art import *: This imports everything from the art module, which is likely used for text decorations and fonts.
3. Word Lists:
   word_list = [["cat", "dog", "car", "cot", "map"], ["high","good","hair","mope","your"],["earth","space","spark","shine","elite"],["friday","forest","castle","prince","silver"],["areesha","sparkle","journey","fantasy","diamond"]]
This defines a list of word lists, with each sublist corresponding to a different level of difficulty or stage in the game.
4. Title Display:
   tprint("HANGMAN", font="fancy5", decoration="random")
This prints the title "HANGMAN" with a fancy font and random decoration using the art module.
5. Player's Name:
   name = input("enter your name")
tprint(f"welcome to hangman {name}", font="fancy6", decoration="random")
The program asks for the player's name and then welcomes them with a decorated message.
6. Game Initialization:
   sco = 0
st = []
7. Main Game Loop:
   for i in range(4):
Loops through 4 levels of the game.
8. Random Word Selection:
randoom = list(random.choice(word_list[i]))
tprint(f"level {i + 1}", font="fancy5", decoration="random")
st = []
for j in range(len(randoom)):
    st += '.'
Chooses a random word from the current level's word list, prints the level number, and initializes the st list with dots representing each letter of the chosen word.
9. Guessing Loop:
score = 100
for o in range(score//len(word_list[i])):
Sets an initial score of 100 and starts a loop that runs a certain number of times based on the word list length.
10. Player Input:
f = input("enter letter:")
Prompts the player to guess a letter.
11. Checking the Guess:
for k in range(len(randoom)):
    if f == randoom[k] and not st[k] == f:
        st[k] = f
        score += 10
        break
    else:
        score = score - 1
Checks if the guessed letter is in the random word. If correct, updates the corresponding position in st and increases the score. Otherwise, decreases the score.
12. Display Current State:
for l in range(len(st)):
    print(st[l], end='')
print()
print(score)
Prints the current state of the guessed word and the score.
13. Check Win Condition:
if not '.' in st:
    sco += score
    break
Checks if the player has guessed the entire word. If yes, adds the current score to the total score and breaks out of the loop.
14. Final Check:
if st == random:
    print("You Won")
    print('total', sco)
    for i in range(len(st)):
        print(st[i], end='')
After the loop, checks if the player won, prints a winning message, the total score, and the final guessed word.
In summary, this code implements a basic version of the hangman game with different levels, random word selection, and scoring based on the player's guesses. The art module is used to print fancy messages, enhancing the visual appeal of the game.
