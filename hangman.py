import time
import random

def main():
    turns = 10
    print("Hello, Let's play hangman! You will have " + str(turns) + ' turns!')
    print('')
    time.sleep(0.5)
    wordList = ['hehe', 'this', 'is', 'just', 'a', 'python', 'hangman', 'game']
    word = random.choice(wordList)
    guesses = ''
    while turns > 0:
        wrong = 0
        for char in word:
            if char in guesses:
                print(char),
            else:
                print('_'),
                wrong += 1
        print('\n')
        if wrong == 0:
            print('You won :)')
            again = input("Do you want to play again? y/n\n")
            if again == 'y':
                main()
            else:
                exit()
        print('\n')
        guess = ''
        if len(guess) < 1:
            guess = input('Guess a character or enter the correct word: ')[0]
        guesses += guess
        if guess not in word:
            turns -= 1
            print('Wrong')
            print('You have', + turns, ' turns left!')
            if turns == 0:
                print('You Lose :(')

main()