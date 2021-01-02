from random_words import RandomWords
import random
import string

r = RandomWords()

def get_random_word():
    word = r.random_word()
    return word

def play():
    word = get_random_word().upper()
    lives = 6
    word_letters = set(word)
    alphabet = set(string.ascii_letters)
    used_letters = set()
    while len(word_letters)>0 and lives > 0:
        print("You have used these letters: ", " ".join(used_letters))   
        word_list= [letter if letter in used_letters else '_' for letter in word]
        print("current word: ", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:       
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                if(lives>0):
                    lives-=1
                    hangman = display_hangman(lives)
                    print(hangman)
        elif user_letter in used_letters:
            print("You already have used this letter. Try again")
        else:
            print("invalid character")
            
    if lives == 0:
        print("sorry you have died, the word was ", word)
    else:
        print('Yay! you guessed the word ', word)
            
            
def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]


play()
    