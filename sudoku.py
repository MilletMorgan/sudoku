#a if condition else b

import random
import platform
from os import system

grid = [
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
]

#grid = [[0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0]]

chosenBox = -1
chosenNumber = -1
turn = 0

def play():
    chosenBox = -1
    chosenNumber = -1

    while (chosenBox <= 0 or chosenBox >= 81):
        try:
            print('')
            chosenBox = int(input('Choose the box you want put a number between 0 and 81 : '))
            if(grid[chosenBox] > 0):
                print('Case already use')
                play()
            chosenNumber = int(input('Chose your number between 0 and 9 : '))
            if(chosenNumber <= 0 or chosenNumber > 9):
                print('Please, choose a number between 0 and 9.')
                play()

            print('\n')
            grid[chosenBox] = chosenNumber

            printGame()
            play()

        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Bad choice')

    print(grid[randomBox][randomNumber])

def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def printGame():
    global turn

    if (turn == 0):
        if(chosenNumber <= 0 or chosenNumber > 9):
            randomGrid()
        turn += 1

    print("1  B  C    D  E  F    G  H  I")
    print('----------------------------- \n')

    i = 0

    while(i <= 80):
        print(grid[i], ' ', end= "")
        i+=1
        if(i == 3):
            print('* ', end="")
        elif(i == 6):
            print('* ', end="")
        elif(i == 9):
            print('\n','---------------------------')
        elif(i == 12):
            print('* ', end="")
        elif(i == 15):
            print('* ', end="")
        elif(i == 18):
            print('\n','---------------------------')
        elif(i == 21):
            print('* ', end="")
        elif(i == 24):
            print('* ', end="")
        elif(i == 27):
            print('\n','***************************')
        elif(i == 30):
            print('* ', end="")
        elif(i == 33):
            print('| ', end="")
        elif(i == 36):
            print('\n','---------------------------')
        elif(i == 39):
            print('* ', end="")
        elif(i == 42):
            print('| ', end="")
        elif(i == 45):
            print('\n','---------------------------')
        elif(i == 48):
            print('| ', end="")
        elif(i == 51):
            print('| ', end="")
        elif(i == 54):
            print('\n','***************************')
        elif(i == 57):
            print('| ', end="")
        elif(i == 60):
            print('| ', end="")
        elif(i == 63):
            print('\n','---------------------------')
        elif(i == 66):
            print('| ', end="")
        elif(i == 69):
            print('| ', end="")
        elif(i == 72):
            print('\n','---------------------------')
        elif(i == 75):
            print('| ', end="")
        elif(i == 78):
            print('| ', end="")
        elif(i == 81):
            print('\n')

def randomGrid():
    global grid
    randomBox = 0
    randomNumber = 0

    a = 0

    while (a <= 81):
        randomBox = random.randint(0,81)
        randomNumber = random.randint(1,9)

        grid[randomBox] = randomNumber

        a+=1

def main():
    clean()
    printGame()
    play()


if __name__ == '__main__':
    main()
