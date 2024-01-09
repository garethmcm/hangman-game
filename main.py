import random
import string

import os

def process_text(in_file, out_file):

#processes text file to remove unnecessary punctuation, creates new text file without and with words on new lines

    try:
        with open(in_file) as file:
            content = file.read()

        words = content.replace('"', ' ').replace(',',' ').split()

        if not os.path.isfile(out_file):
            with open(out_file, 'w') as file:
                for word in words:
                    file.write(word + '\n')

        else:
            print(f"File already exists")

    except FileNotFoundError:
        print(f"File not found")

        with open(out_file) as file:
            for word in words:
                file.write(word + '\n')

def get_valid_word():
# returns valid word from file for parsing

    #load text file unparsed
    in_words = 'words.txt'
    #file for output content
    out_words = 'output_words.txt'

    # parse text file
    process_text(in_words, out_words)

    with open(out_words) as file:
        words = [line.strip() for line in file]

    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
#hangman game - word returned, set to uppercase and used_letters initialised

    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, ' lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print('\nLetter ', user_letter, ' is not in word')

        elif user_letter in used_letters:
            print('You have tried this already')

        else:
            print('Invalid character, please try again')

    if lives == 0:
        print('Woops, you died. The word was ', word)
    else:
        print('You dancer. You guessed the word ', word)

if __name__ == '__main__':
    hangman()