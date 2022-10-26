import random
import hangman_words
import hangman_arts
import sys
from replit import clear
#step1: generating words

print(hangman_arts.logo)
print('\n')
word_choosen = hangman_words.word_list[random.randint(0,len(hangman_words.word_list)-1)] ##choosing a random word from the list
flag= False
#step 2 : generating blanks
lives =6
display =[]
for i in word_choosen:
    display.append("_")
print(' '.join(display))
while ("_" in display):

    if (lives==0):
        print("you loose")
        print("THE WORD WAS {}".format(word_choosen))
        exit()
        break

    guess=input("enter a letter ")
    clear()
    if(guess in display):
        print("you have already entered '{}' before please select another word".format(guess))
        continue
    flag=0
    for i in range(0,len(word_choosen)):
        if (word_choosen[i] == guess):
            display[i]=guess
            flag=1
    if(flag==0):
        print("THE LETTER '{}' IS NOT IN THE WORD PLEASE TRY AGAIN".format(guess))
        lives=lives-1
        print("Lives left={}".format(lives))
    print(' '.join(display))
    print(hangman_arts.stages[lives])

print("YAY! YOU WON")

