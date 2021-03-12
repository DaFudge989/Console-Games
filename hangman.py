import random

images = [
    """






    """,
    """
    




    ________
    """,
    """
    
    |
    |
    |
    |
    ________
    """,
    """
     ___
    |
    |
    |
    |
    ________
    """,
    """
     ___
    |   |
    |
    |
    |
    ________
    """,
    """
     ___
    |   |
    |   o
    |
    |
    ________
    """,
    """
     ___
    |   |
    |   o
    |   +
    |
    ________
    """,
    """
     ___
    |   |
    |   o
    |   +
    |   /
    ________
    """,
    """
     ___
    |   |
    |   o
    |   +
    |   /\\
    ________
    """,
]

def makeList(file):
    wordlist = []
    words = open(file, 'r')
    for i in words:
        line = i.split(', ')
        wordlist = wordlist + line
    return wordlist

def indexer(toIndex):
    copy = toIndex
    indexed = {}
    for i in range(len(toIndex)):
        if toIndex[i] in indexed:
            indexed[toIndex[i]].append(i)
        else:
            indexed[toIndex[i]] = [i]
    return indexed

easyList = makeList('/Users/oliver.price/Documents/IST/Yr 11 Portfolio/Console Games/easyWords.txt')
mediumList = makeList('/Users/oliver.price/Documents/IST/Yr 11 Portfolio/Console Games/mediumWords.txt')
hardList = makeList('/Users/oliver.price/Documents/IST/Yr 11 Portfolio/Console Games/hardWords.txt')
options = {'easy':easyList, 'medium':mediumList, 'hard':hardList}

def main():
    print('What difficulty do you want to play?')
    difficulty = input('easy, medium or hard? ')
    while difficulty not in options:
        print('Not valid')
        difficulty = input('easy, medium or hard? ')
    word = [char for char in random.choice(options[difficulty])]
    index = indexer(word)
    guesslist = []
    unsolved = []
    incorrectGeusses = 0
    for i in range(len(word)):
        unsolved.append('-')
    while True:
        print(images[incorrectGeusses])
        print(''.join(unsolved))
        print('Guesslist: ' + ', '.join(guesslist))
        while True: 
            guess = input('Guess a letter ')
            if guess.isalpha() != True or len(guess) != 1:
                print('Not a valid answer')
                continue
            elif guess in guesslist or guess in word and guess in unsolved:
                print('You\'ve already guessed this letter')
                continue
            elif guess not in guesslist and guess not in word:
                incorrectGeusses += 1
                guesslist.append(guess)
                print('Incorrect guess,', 8-incorrectGeusses, 'guesses remaining') if incorrectGeusses != 7 else print('Incorrect guess, only 1 guess left')
                break
            elif guess in word and guess not in unsolved:
                for i in index[guess]:
                    unsolved[i] = guess
                print('Correct guess!')
                break
        if unsolved == word:
            print('You Won!!!')
            break
        if incorrectGeusses == 8:
            print('You lose')
            break

def playAgain():
    print('Do you want to play again?')
    options = ['yes', 'no']
    answer = input('yes or no? ')
    while answer not in options:
        print('Not valid')
        answer = input('yes or no? ')
    if answer == 'yes':
        main()

if __name__ == '__main__':
    main()
    playAgain()