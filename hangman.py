import random

def generate_hangman_word():
    HANGMAN_WORDS = [
        'agree',
        'native', 
        'dead',
        'ethnic',
        'coach',
        'fault',
        'heat',
        'referee',
        'forge',
        'broken',
        'faint',
        'shy',
        'freeze',
        'rotten',
        'wine'
  ]
    hangman_word = random.choice(HANGMAN_WORDS)
    return hangman_word

def print_failed_attempts_0():
    print("   +---+")
    print("       |")
    print("       |")
    print("       |")
    print("       ===")
  
def print_failed_attempts_1():
    print("   +---+")
    print("   O   |")
    print("       |")
    print("       |")
    print("       ===")

def print_failed_attempts_2():
    print("   +---+")
    print("   O   |")
    print("   |   |")
    print("       |")
    print("       ===")

def print_failed_attempts_3():
    print("   +---+")
    print("   O   |")
    print("  /|   |")
    print("       |")
    print("       ===")

def print_failed_attempts_4():
    print("   +---+")
    print("   O   |")
    print("  /|\  |")
    print("       |")
    print("       ===")

def print_failed_attempts_5():
    print("   +---+")
    print("   O   |")
    print("  /|\  |")
    print("  /    |")
    print("       ===")

def print_failed_attempts_6():
    print("   +---+")
    print("   O   |")
    print("  /|\  |")
    print("  / \  |")
    print("       ===")
    print('You LOSE!')

FAILED_ATTEMPTS = 0
LETTERS_USED = []

hangman_word = generate_hangman_word()
print_failed_attempts_0()

while FAILED_ATTEMPTS < 6:
    letter_input = input('> Choose a letter: ')
    if letter_input in LETTERS_USED:
        print('You have already used this letter')
    elif len(letter_input) != 1:
        print('The length of input must be only 1')
    else:
        LETTERS_USED.append(letter_input)
        if letter_input not in hangman_word:
            FAILED_ATTEMPTS += 1

    if FAILED_ATTEMPTS == 0:
        print_failed_attempts_0()
    elif FAILED_ATTEMPTS == 1:
        print_failed_attempts_1()
    elif FAILED_ATTEMPTS == 2:
        print_failed_attempts_2()
    elif FAILED_ATTEMPTS == 3:
        print_failed_attempts_3()
    elif FAILED_ATTEMPTS == 4:
        print_failed_attempts_4()
    elif FAILED_ATTEMPTS == 5:
        print_failed_attempts_5()
    elif FAILED_ATTEMPTS == 6:
        print_failed_attempts_6()
        print(f'=== You lost ===')
        break

    CURRENT_GUESS = []
    for index, hangman_letter in enumerate(hangman_word):
        if hangman_letter in LETTERS_USED:
            CURRENT_GUESS.insert(index, hangman_letter)
        else:
            CURRENT_GUESS.insert(index, '*')
    CURRENT_GUESS = ''.join(CURRENT_GUESS)

    print(f'Hangman word is: {hangman_word}')
    print(f'Current guess: {CURRENT_GUESS}')
    print(f'Letters used: {LETTERS_USED}')
    if CURRENT_GUESS == hangman_word:
        print(f'=== You win on {FAILED_ATTEMPTS} failed attempt(s) ===')
        break