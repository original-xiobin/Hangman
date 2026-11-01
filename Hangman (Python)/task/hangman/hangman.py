import random
from enum import Enum

MAX_GUESSES = 8
RESULTS = {'wins': 0, 'losses': 0}

is_running = True

class Selection(Enum):
    PLAY = 'play'
    RESULTS = 'results'
    EXIT = 'exit'

def contains_letter(letter, word):
    return letter in word

def update_guess_word(letter, word, guess_word):
    new_guess_word = ''
    for i in range(len(word)):
        if word[i] == letter:
            new_guess_word += letter
        else:
            new_guess_word += guess_word[i]
    return new_guess_word

def is_valid(answer, guessed_letters):
    if len(answer) != 1:
        print('Please, input a single letter.\n')
        return False
    elif not answer.islower():
        print('Please, enter a lowercase letter from the English alphabet.\n')
        return False
    elif answer in guessed_letters:
        print('You\'ve already guessed this letter.\n')
        return False
    return True

def show_results():
    print(f'You won: {RESULTS["wins"]} times.')
    print(f'You lost: {RESULTS["losses"]} times.')

def play():
    guesses_left = MAX_GUESSES
    guessed_letters = []
    words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(words)
    guess_word = len(word) * '-'

    while guesses_left > 0:
        print(guess_word)
        answer = input(f'Input a letter: ')
        if not is_valid(answer, guessed_letters):
            continue
        if contains_letter(answer, word):
            guess_word = update_guess_word(answer, word, guess_word)
            if guess_word == word:
                print(f'You guessed the word {guess_word}!\nYou survived!')
                RESULTS['wins'] += 1
                break
            else:
                print()
        else:
            guesses_left -= 1
            post_fix = (f'# {guesses_left} '
                        + 'attempts' if guesses_left > 1 else f'# {guesses_left} '
                        + 'attempt')
            if contains_letter(answer, guess_word):
                print('No improvements.  ' + post_fix + '\n')
            else:
                print('That letter doesn\'t appear in the word.  ' + post_fix + '\n')
        guessed_letters.append(answer)

    if contains_letter('-', guess_word):
        print('You lost!')
        RESULTS['losses'] += 1

print('H A N G M A N # 8 attempts')
while is_running:
    answer = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if answer in [item.value for item in Selection]:
        match answer:
            case Selection.PLAY.value:
                print()
                play()
            case Selection.RESULTS.value:
                show_results()
            case Selection.EXIT.value:
                is_running = False
    else:
        continue