import random
import string
import string
from words import words

def hangman():
    word = get_valid_word(words['data'])
    print(word)
    guessLetters(word)

    
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        print(word)
        word = random.choice(words)
    return word

def guessLetters(word):
    word_letters = set(word.lower())
    used_letters = set()
    alphabet = set(string.ascii_lowercase)
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives left. \n You have already used these letters: ' ,''.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ' ,' ' . join(word_list))
        letter = input("guess letter")
        if letter in alphabet - used_letters and letter in word_letters:
            word_letters.remove(letter)
            used_letters.add(letter)
        elif letter in alphabet - used_letters and letter not in word_letters:
            used_letters.add(letter)
            lives = lives - 1
            print(f"Letter {letter} not in word please try again")
        elif letter in used_letters:
            print(f"You already used the letter {letter}")
        else:
            print(f"{letter} is not a valid letter")

    if len(word_letters) == 0:
        print(f"Word completed: {word}")
    else:
        print(f"oops game over you have no more lives the word was {word} try again")
    
    






if __name__ == '__main__':
    hangman()