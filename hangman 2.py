import random
from art import *
word_list = [["cat", "dog", "car", "cot", "map"], ["high","good","hair","mope","your"],["earth","space","spark","shine","elite"],["friday","forest","castle","prince","silver"],["areesha","sparkle","journey","fantasy","diamond"]]


tprint("HANGMAN", font="fancy5", decoration="random")
name=(input("enter your name"))
tprint(f"welcome to hangman {name}", font = "fancy6", decoration="random")
sco=0
st = []
for i in range(4):
    randoom='h'
    del randoom
    randoom = list(random.choice(word_list[i]))
    tprint(f"level {i + 1}", font="fancy5", decoration="random")
    st = [];
    for j in range(len(randoom)):
        st += '.'
    score = 100
    for o in range(score//len(word_list[i])):
        print("Guess The Word")
        f = input("enter letter:")
        for k in range(len(randoom)):
            if f == randoom[k] and not st[k] == f:
                st[k] = f
                score += 10
                break
            else:
                score = score-(1)
        for l in range(len(st)):
            print(st[l], end='')
        print()
        print(score)



        if not '.' in st:
            sco += score
            break


if st == random:
    print("You Won")
    print('total', sco)
    for i in range(len(st)):
        print(st[i], end='')
