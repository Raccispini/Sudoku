import random
import os,sys
sys.setrecursionlimit(15000)
c_max = 2000
def creaSudoku(dimension):
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

def check(sudoku):
    
    #Controlla righe
    for i in range(0,len(sudoku)):
        for j in range(0,len(sudoku)):
            for k in range((j+1),len(sudoku)):
                if sudoku[i][j]==sudoku[i][k] and sudoku[i][j]!=0:
                    #print(str(sudoku[i][j])+" = "+ str(sudoku[i][k]))
                    return False
    #Controlla colonne(o l'inverso cazzo ne so)
    for i in range(0,len(sudoku)):
        for j in range(0,len(sudoku)):
            for k in range((j+1),len(sudoku)):
                if sudoku[j][i]==sudoku[k][i] and sudoku[j][i]!=0:
                    #print(str(sudoku[j][i])+" = "+ str(sudoku[k][i]))
                    return False
    #Controlla celle
    n = [0,0,0,0,0,0,0,0,0]
    for l in [0,3,6]:
        for k in [0,3,6]:
            n = [0,0,0,0,0,0,0,0,0]
            for i in len(sudoku):
                for j in len(sudoku):
                    if n[sudoku[i][j]+1]!=0:
                        n[sudoku[i][j]+1]=sudoku[i][j]
                    else:
                        return False
    return True
    
def randomFill(sudoku,n):
    print("Generazione Sudoku . . .")
    new_sudoku = sudoku
    c=0
    while(True):

        if check(new_sudoku):
            sudoku = new_sudoku
            new_sudoku[random.randint(0,len(sudoku)-1)][random.randint(0,len(sudoku)-1)]= random.randint(1,9)
            c=c+1
        else:
            new_sudoku = sudoku
        if check(new_sudoku) and c==n:
            print("Sudoku generato !!")
            return new_sudoku
        elif c == n:
            #stampaSudoku(sudoku)
            sudoku = azzera(sudoku)
            c=0

def azzera(sudoku):
    #print("Azzeramento Sudoku . . .")
    for i in range(0,len(sudoku)):
        for j in range(0,len(sudoku)):
            sudoku[i][j]=0
    #print("Sudoku azzerato!!")
    return sudoku
##############################################################################
def risolvi(sudoku):
    c1 = 0
    c2 = 0
    new_sudoku = sudoku
    new_sudoku1 = sudoku
    while(checkColonne(sudoku)):
        for i in range(0,len(sudoku)):
            while(not checkRowFull(sudoku,i)):
                for j in range(0,len(sudoku)):
                    if(sudoku[i][j]==0):
                        k =random.randint(1,9)
                        a =True
                        while(findNumInRow(sudoku,i,k) and a):
                            a = True
                            k = random.randint(1,9)
                            if  not findNumInRow(sudoku,i,k):
                                new_sudoku[i][j]=k
                                if(checkColonne(new_sudoku)):
                                    new_sudoku1=new_sudoku
                                    break
                                else:
                                    new_sudoku = new_sudoku1
                                    a=False
                            c = c+1
                            if(c>c_max):
                                new_sudoku = sudoku
                                new_sudoku1 = sudoku
                                c=0
                        stampaSudoku(new_sudoku1)   
    return new_sudoku
##############################################################################
def checkColonne(sudoku):
    for i in range(0,len(sudoku)):
        for j in range(0,len(sudoku)):
            for k in range((j+1),len(sudoku)):
                if sudoku[j][i]==sudoku[k][i] and sudoku[j][i]!=0:
                    #print(str(sudoku[j][i])+" = "+ str(sudoku[k][i]))
                    return False
    return True

def checkRow(sudoku,row):
    for i in range(0,len(sudoku)):
        for j in range(0,len(sudoku)):    
            if sudoku[row][i]==sudoku[row][j] and sudoku[row][i]!=0:
                return False
def findNumInRow(sudoku,row,num):
    for j in range(0,len(sudoku)):    
        if sudoku[row][j]==num:
            return True
    return False
def findNumInColumn(sudoku,column,num):
    for j in range(0,len(sudoku)):    
        if sudoku[j][column]==num:
            return True
    return False
def checkRowFull(sudoku,row):
    for i in range(0,len(sudoku)):
        if sudoku[row][i] == 0:
            return False
    return True
def checkFull(sudoku):
    for i in range(0,len(sudoku)):
        for j in range(0,len(sudoku)):
            if sudoku[i][j]==0:
                return False
    return True
def risolviSpazi(sudoku):
    while(checkFull(sudoku)):
        for k in range(1,9):
            for i in range(0,len(sudoku)):
                for j in range(0,len(sudoku)):
                    if sudoku[i][j]!=0:
                        if findNumInRow(sudoku,j,k) and findNumInColumn(sudoku,i,k):
                            sudoku[i][j] = k

                stampaSudoku(sudoku)
    return sudoku
def generazioneSudokuCompleto():
    sudoku = creaSudoku(9)
    num = [1,2,3,4,5,6,7,8,9]
    print(len(num))
    #while(True):
    sudoku = azzera(sudoku)
    for i in range(0,len(sudoku)):
        num = [1,2,3,4,5,6,7,8,9]
        for j in range(0,len(sudoku)):
            while True:
                r = random.randint(0,len(num)-1)
                n = num[r]  
                if findNumInColumn(sudoku,j,n) and findNumInRow(sudoku,i,n):
                    sudoku[i][j] = n
                    num = num.remove(n)
                    break
                stampaSudoku(sudoku)
    if checkFull(sudoku): 
        if check(sudoku):
            return sudoku
def findInArray(array,n):
    for i in range(0,len(array)):
        if array[i]==n:
            return True
    return False

def getPossibleNumber(sudoku,row,column):
    n = [1,2,3,4,5,6,7,8,9]
    estratti = []
    for i in range(0,len(sudoku)):
        if sudoku[row][i]!=0:
            if not findInArray(estratti,sudoku[row][i]):
                estratti.append([sudoku[row][i]])
                
                if findInArray(n,sudoku[row][i]):
                    n.remove(sudoku[row][i])

    for i in range(0,len(sudoku)):
        if sudoku[i][column]!=0:
            if not findInArray(estratti,sudoku[row][i]):
                estratti.append([sudoku[i][column]])
                if findInArray(estratti,sudoku[row][i]):
                    n.remove(sudoku[i][column])
    l=0
    k =0
    #Cerca la cella di appartenenza
    if row in range(0,2):
        k = 0
    if row in range(3,5):
        k = 3
    if row in range(6,8):
        k = 6
    if column in range(0,2):
        l = 0
    if column in range(3,5):
        l = 3
    if column in range(6,8):
        l = 6 
    #Controllo celle
    for i in range(0,2):
        for j in range(0,2):
            if sudoku[k+i][l+j]!=0:
                if not findInArray(estratti,sudoku[k+i][l+j]):
                    estratti.append(sudoku[k+i][l+j])
                    
                    if findInArray(n,sudoku[k+i][l+j]):
                        n.remove(sudoku[k+i][l+j])
    print("column = "+str(column)+"   row =   "+str(row))
    print(n)
    return n


def backTrack(sudoku):
    s = sudoku
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if s[i][j]==0:
                n = getPossibleNumber(s,i,j)
                if len(n)==0:
                    return backTrack(sudoku)
                else:
                    s[i][j]= n[random.randint(0,len(n)-1)]
                    stampaSudoku(s)

    return s

os.system('cls')
board = creaSudoku(9)
board = backTrack(board)
stampaSudoku(board)
#stampaSudoku(risolviSpazi(board))