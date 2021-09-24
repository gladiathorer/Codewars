import numpy as np
import random


def queenPos(table,j):
    #returns a tuple of the coordinates where cell is 1
    for i in range(len(table)):
        if table[(i,j)] == 1:
            return (i,j)
        
def queensPos(table):
    #return a list of tuples of the coordinates where the cell is 1
    mylist = []
    for i in range(len(table)):
        for j in range(len(table)):
            if table[(i,j)] == 1:
                mylist.append((i,j))
    return mylist


def cost(table,queen_pos):
    if queen_pos == None:
        return 0
    cost = 0
    queens = queensPos(table)
    for queen in queens:
        if queen[0] == queen_pos[0] and queen != queen_pos:
            cost+=1
        if queen[1] == queen_pos[1] and queen != queen_pos:
            cost+=1
        if abs(queen[0] - queen_pos[0]) == abs(queen[1] - queen_pos[1]) and queen != queen_pos:
            cost+=1
    return cost

        
def queens(position, size):
    table = np.zeros((size,size),int)
    poz = (['a','b','c','d','e','f','g','h','i','j'].index(position[0]),size - int(position[1]))
    while True:
        queens = queensPos(table)
        if len(queens) == size:
            costi = 0
            for queen in queens:
                if (cost(table,queen)) !=0:
                    costi+=1
            if costi == 0:
                mylist = []
                for queen in queens:
                    str1 = ['a','b','c','d','e','f','g','h','i','j'][queen[0]]
                    str2 = str(size-queen[1])
                    mylist.append(str1+str2)
                for i in range(len(mylist)):
                    if len(mylist[i]) == 3:
                        mylist[i] = mylist[i][0] + '0'
                return ','.join(mylist)
                    
        j = random.randint(0,size-1)
        if j !=poz[1]
            for i,j in [(i,j) for i in range(size)]:
                #print(table)
                queen_pos = queenPos(table,j)
                #print(table)
                cost_before = cost(table, queen_pos)
                #print(table)
                if queen_pos != None:
                    table[queen_pos] = 0
                #print(table)
                table[(i,j)] = 1
                #
                if cost(table, queenPos(table,j)) > cost_before:
                    if queen_pos != None:
                        table[(i,j)] = 0
                        table[queen_pos] = 1
