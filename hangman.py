import random
from string import ascii_lowercase

word_list = ['python', 'java', 'kotlin', 'javascript']
ran_word = random.choice(word_list)
set_word = set(ran_word)
list_word = list(ran_word)
hidden = ["-" for i in ran_word]
lives = 8  # decrease when player guess wrong
score = 0  # increases when player guess right letter
abs_wrong = []  # contains all letters not in the random word


def hangman(letter):
    """The function defines the game rules for the popular hangman game"""
    global ran_word, set_word, list_word, hidden, lives, score, abs_wrong
    if letter in set_word:
        set_word.discard(letter)
        for let in list_word:
            if let == letter:
                hidden[list_word.index(letter)] = letter
                list_word[list_word.index(letter)] = "-"
                score += 1
                if score == len(ran_word):
                    lives = 0  # sets "lives" to zero (0) to terminate the current game session
                    print("You guessed the word!", "You survived!", sep="\n")
    elif letter not in ran_word:
        if letter not in abs_wrong:  # checks if letter not already guessed
            abs_wrong.append(letter)
            lives -= 1
            print("No such letter in the word")
            if lives == 0:
                print("You are hanged!", sep='\n')
        else:
            print("You already typed this letter")
    else:
        print("You already typed this letter")
        if lives == 0:
            print("You are hanged!", sep='\n')


def game_menu():
    """"The function defines the start menu of ghe game"""
    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu == "play":
        return True
    else:
        return False


def play_game():
    """The function starts the game if user wants to play"""
    global hidden, lives
    print("H A N G M A N")
    while lives > 0:
        print()
        print(''.join(hidden))
        guess = input("Input a letter:")
        if len(guess) == 1 and guess in ascii_lowercase:
            hangman(guess)
        elif len(guess) == 1 and guess not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        else:
            print("You should input a single letter")


start = True
while start:
    if game_menu() is True:
        play_game()
    else:
        start = False
