#ternary conditional : a if condition else b

import random
import platform
from os import system

chosenBox = -1
chosenNumber = -1
turn = 0

#n = 9
#grid = [[0] * n for i in range(n)]

grid = [
        [4, 0, 0, 5, 0, 1, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 2, 0, 9],
        [9, 6, 0, 0, 0, 7, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 7, 2, 6, 9, 0, 0],
        [5, 0, 0, 9, 8, 0, 0, 6, 0],
        [0, 7, 1, 0, 0, 8, 5, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
]

"""
[4, 2, 8, 5, 9, 1, 6, 3, 7],
[3, 1, 7, 8, 6, 4, 2, 5, 9],
[9, 6, 5, 2, 3, 7, 8, 1, 4],
[7	9	6   4	1	5   3	2	8],
[1	8	3   7	2	6   9	4	5],
[5	4	2   9	8	3   7	6	1],
[2	7	1   3	4	8   5	9	6],
[8	3	4   6	5	9   1	7	2],
[6	5	9   1	7	2   4	8	3]
"""

"""
grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
"""
def play():
    chosenBoxX = -1
    chosenBoxY = -1
    chosenNumber = -1

    global grid

    printGame()

    while (chosenBoxX <= 0 or chosenBoxX >= 9):
        try:
            chosenBoxX = int(input('Choose the box on the abscisse you want put a number between 0 and 8 : '))
            chosenBoxY = int(input('Choose the box on the ordinate you want put a number between 0 and 8 : '))
            chosenNumber = int(input('Chose your number between 0 and 9 : '))

            printGame()
            print('')

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
    i = 0
    e = 0
    ordonate = 0

    clean()

    print("Abscisse (012345678) -->")
    print("Ordinate (012345678)")
    print("|")
    print("|")
    print("V")
    print("O/A| 0   1   2   3   4   5   6   7   8")
    print("---------------------------------------")

    for row in grid:
        print(ordonate, " | ", end="")
        print("   ".join([str(elem) for elem in row]))
        print("")
        ordonate+=1

        if ordonate == 3 or ordonate == 6:
            print("***************************************")
        #else:
        #    print("---------------------------------")

        i+=1

"""
def randomGrid():
    global grid
    n = 9
    a = 0
    grid = [[0] * n for i in range(n)]
    difficulty = 36

    while (a < difficulty):
        x = random.randint(0,8)
        y = random.randint(0,8)
        randomNumber = random.randint(1,9)
        listeChiffres = [1,2,3,4,5,6,7,8,9]
        tabChiffresDejaPresents = []

        for row in grid:
            for chiffre in listeChiffres:
                if grid[x].count(chiffre) > 1:
                    for row in grid:
                        if grid[y][x] == chiffre:
                            tabChiffresDejaPresents.append([y,x])
                else:
                    grid[y][x] = randomNumber



        if grid[y][x] == 0:
            grid[y][x] = randomNumber
        elif grid[y][x] != 0:
            continue

        a+=1
"""

def verifWin():
    tabCol = []
    a = 0

    for row in grid:
        for elem in row:
            if elem == 0:
                continue
            else:
                rowValidate = 1

    while elementCol == 9:
        grid[y][elementCol]
        tabCol.append(elementCol)
        tabColVerif = tabCol.count(a)
        a+=1
        elementCol+=1

        if tabColVerif > 0:
            colValidate = 1




def main():
    clean()
    #randomGrid()
    play()

if __name__ == '__main__':
    main()
