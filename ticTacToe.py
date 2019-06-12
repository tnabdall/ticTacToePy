# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 08:08:13 2019

@author: 826506
"""
import re

def isPositiveNumber(num):
    return True if type(re.match("^\\d+$",num))== re.Match else False

def initializeMatrix(size):
    return [[' ']*size for i in range(size)]

def printBoard(matrix):
    for i in range(len(matrix)):
        if(i!=0):
            print("- "*len(matrix[0]))
        print(*matrix[i], sep="|")

def place(matrix, letter, row, col):
    matrix[row][col] = letter

def checkWin(matrix):
    letterCheck = ""
    win = False

    #check row wins
    for i in range(len(matrix)):
        letterCheck = matrix[i][0]
        if(letterCheck!=" "):
            win = True
            for j in range(1,len(matrix[i])):
                if(matrix[i][j]!=letterCheck):
                    win = False
                    break
            if(win == True):
                return letterCheck
    
    letterCheck = ""
    
    #check col wins
    for j in range(len(matrix[0])):
        letterCheck = matrix[0][j]
        if(letterCheck!=""):
            win = True
            for i in range(1,len(matrix)):
                if(matrix[i][j]!=letterCheck):
                    win = False
                    break
            if(win == True):
                return letterCheck

    #check diagonals
    letterCheck = matrix[0][0]
    if(letterCheck!=""):
        win = True
        for i in range(1, len(matrix)):
            if(matrix[i][i]!=letterCheck):
                win = False
                break
        if(win == True):
                return letterCheck
    
    letterCheck = matrix[0][len(matrix)-1]
    if(letterCheck!=""):
        win = True
        for i in range(len(matrix)-1):
            if(matrix[len(matrix)-i-1][i]!=letterCheck):
                win = False
                break
        if(win == True):
                return letterCheck

    return " " # This will be condition for game not won


def playGame(boardSize):
    board = initializeMatrix(boardSize)
    turn = 'x'
    counter = 0
    while(checkWin(board)==" " and counter<boardSize**2):
        print("It is "+turn+"'s turn. Enter row: ",end="")
        row = input()
        while(isPositiveNumber(row)==False or int(row)<1 or int(row)>len(board)):
            row = input("Error in row selection. Input row: ")
        col = input("Enter col: ")
        while(isPositiveNumber(col)==False or int(col)<1 or int(col)>len(board)):
            col = input("Error in col selection. Input col: ")
        row = int(row)-1
        col = int(col)-1
        if(board[row][col]!=" "):
            print("Error in selection. Space is already occupied.")
        else:
            place(board,turn,row,col)
            turn = 'o' if turn=='x' else 'x'
            counter+=1
        printBoard(board)

    if(counter>=boardSize**2):
        print("It's a tie!")
    else:
        turn = 'o' if turn=='x' else 'x'
        print("The winner is "+turn)

if __name__ == "__main__":
    playGame(3)
    # print(isPositiveNumber("8"))
