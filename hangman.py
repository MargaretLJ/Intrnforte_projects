import random
import string


def get_word(): # to select a random word from the file
    wordlist = []
    with open("wordslist.txt",'r') as file:
        wordlist = file.read().split('\n') # adds each word on the new line to a list
    word = random.choice(wordlist)
    return word.upper()


print("Welcome to hangman!!!!, Let's begin\n--------------------------")

def hangman():
    word=get_word()
    word_letters=set(word) #set of letters in the chosen word
    alphabet =string.ascii_uppercase
    used_letters=set() #handles all the letters the user has tried

    lives = len(word) + 2


    while(len(word_letters)>0 and lives>0):

        print("Lives remaining", lives) 
        print("These are the letters you have guessed:",''.join(used_letters))

        #display the word
        current_word=[letter if letter in used_letters else '_' for letter in word]
        print("Current word :",''.join(current_word))



        user_letter=input("Enter your guess").upper()
        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                print("Sorry, letter ",user_letter, "is not part of the word")
                lives -= 1

        elif user_letter in used_letters:
            print("you already guessed this")

        else:
            print("please enter a valid character")


    if lives==0:
        print("aww sorry , the word was, ",word,". Better luck next time!!")
    else:
        print(word, " was the word . YOU DID IT !!, you didn't kill the man!!")




#Replay the game
if __name__ == "__main__":
    while True:
        hangman()
        x=input("Do you want to replay the game :(Yes or No)").upper()
        if x != "YES":
            break




















