validEntries = '0123456789+-/*()'

def calculator():
    while True:
        line = input('Enter equation: ')
        test = [char for char in line]
        invalid = False
        for i in test:
            if i not in validEntries or len(test) == 1 or test[0].isdigit() == False or test[-1].isdigit() == False:
                print('Not a valid entry')
                invalid = True
                break
        if invalid == True:
            continue
        break
    return eval(line)

            
def playAgain():
    print('Do you want to do another calculation?')
    options = ['yes', 'no']
    answer = input('yes or no? ')
    while answer not in options:
        print('Not valid')
        answer = input('yes or no? ')
    if answer == 'yes':
        main()


def main():
    print('Calculator pog!')
    print('The equation must only contain numbers and valid symbols: +,-,/,*,(,)')
    answer = calculator()
    print(answer)
    playAgain()


main()    