import random
import sys,os
sys.setrecursionlimit(150000)
def creaSudoku():
    dimension = 9
    board = []
    columns = []
    for i in range(0,dimension):
        for j in range(0,dimension):
            columns.append(0)
        board.append(columns.copy())
        columns = []

    return board

def stampaSudoku(sudoku):
    os.system('cls')
    print("  # # # # # # # # # # # # # # # # ")
    print("# ------------------------------ #")
    for i in range(0,len(sudoku)):
        print("# | " ,end = '')
        for j in range(0,len(sudoku)):
            if sudoku[i][j] == 0:
                print(" ", end = ' ')
            else:
                print(str(sudoku[i][j]),end = ' ')
            if (j+1) % 3 == 0 and j != (len(sudoku)-1):
                print(" | ", end = ' ')
        print(" | #")
        if (i+1)%3 == 0:
            print("# ------------------------------ #")
    print("  # # # # # # # # # # # # # # # # ")
    print()
    print(" ------------------------------  ")
    print()



def check(sudoku,n,row,column):
    
    #Controlla righe
    for i in range(0,len(sudoku)):
        if sudoku[row][i]==n and sudoku[row][i]!=0:
            return False
    #Controlla colonne(o l'inverso cazzo ne so)
    for i in range(0,len(sudoku)):
        if sudoku[i][column]== n and sudoku[i][column]!=0:
            return False
    #Controlla celle
    l = row//3
    k = column//3
    for i in range(l*3,l*3+3):
        for j in range(k*3,k*3+3):
            if sudoku[i][j]==n and i != row and j != column and sudoku[i][j]!=0:
                return False
    return True

def findEmpty(sudoku):
    for i in range(0,len(sudoku)):
        for j in range(0,len(sudoku)):
            if sudoku[i][j]==0:
                return (i,j)
    return None

def backTrack(sudoku):
    pos  = findEmpty(sudoku)
    if not pos:
        return True
    else:
        row,col = findEmpty(sudoku)

    for i in range(1,10):
        if check(sudoku,i,row,col):
            sudoku[row][col]=i
            stampaSudoku(sudoku)
            if backTrack(sudoku):
                return True
            
            sudoku[row][col]=0
    return False

def deleteSomeCells(s):
    n = random.randint(30,70)
    for i in range(0,n):
        row = random.randint(0,8)
        col = random.randint(0,8)
        s[row][col]=0
    return s

os.system('cls')
sudoku =[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

backTrack(sudoku)
#sudoku = deleteSomeCells(sudoku)
stampaSudoku(sudoku)