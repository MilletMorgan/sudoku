#ternary conditional : a if condition else b

import random
import platform
from os import system

chosenBox = -1
chosenNumber = -1
turn = 0

n = 9
grid = [[0] * n for i in range(n)]

def play():
    chosenBoxX = -1
    chosenBoxY = -1
    chosenNumber = -1

    while (chosenBoxX <= 0 or chosenBoxX >= 9):
        try:
            printGame()
            print('')
            chosenBoxX = int(input('Choose the box on the abscisse you want put a number between 0 and 8 : '))
            chosenBoxY = int(input('Choose the box on the ordinate you want put a number between 0 and 8 : '))
            chosenNumber = int(input('Chose your number between 0 and 9 : '))

            if ((chosenBoxX < 0) and (chosenBoxX > 8) and (chosenBoxY < 0) and (chosenBoxY > 8)):
                play()
            if(grid[chosenBoxY][chosenBoxX] > 0):
                play()
            if(chosenNumber <= 0 or chosenNumber > 8):
                play()

            print('\n')
            grid[chosenBoxY][chosenBoxX] = chosenNumber

            play()

        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Bad choice')

def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    system('cls') if 'windows' in os_name else system('clear')

def printGame():
    global turn

    clean()

    print("Abscisse (012345678) -->")
    print("Ordinate (012345678)")
    print("|")
    print("|")
    print("V")
    print("---------------------------------")

    for row in grid:
        print(' | '.join([str(elem) for elem in row]))
        print("---------------------------------")

def randomGrid():
    global grid
    randomBox = 0
    randomNumber = 0
    n = 9
    grid = [[0] * n for i in range(n)]
    gridExistingNumber = [[0] * n for i in range(n)]
    difficulty = 36
    a = 0

    while (a <= difficulty):
        x = random.randint(0,8)
        y = random.randint(0,8)
        randomNumber = random.randint(1,9)

        grid[y][x] = 0

        gridExistingNumber = []
        gridExistingNumber.append(x)
        gridExistingNumber.append(y)

        #print(grid[y][x])

        grid[y][x] = randomNumber

        #for elem in gridExistingNumber:
        #    if ((elem == y) and (elem+1 == x)):
        #        randomGrid()
        #    else:
        #        grid[y][x] = randomNumber

        a+=1

def main():
    clean()
    randomGrid()
    play()

if __name__ == '__main__':
    main()
