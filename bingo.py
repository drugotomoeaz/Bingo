# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:46:33 2018

@author: Pandora
"""

from random import sample

class Bingo(object):
    def __init__(self):
        self.numbers = sample(range(1,26), k = 25)
        self.generateBoard()
        
    def generateBoard(self):
        self.board = [[],[],[],[],[]]
        
        for number in range(25):
            self.board[number//5].append(self.numbers[number])
    
    def plotBoard(self):
        for row in self.board:
            print("\n","","-"*25)
            print(" | ", end="")
            for number in row:
                if len(str(number)) > 1:
                    print(number, end = " | ")
                else:
                    print(number, end = "  | ")
        print("\n","","-"*25)
        
        
    def updateBoard(self, choice):

        if choice in self.numbers:
            i = self.numbers.index(choice)
            self.board[i // 5][i % 5] = "X"
            self.numbers[i] = "X"
#            self.plotBoard()
            return True        
        else:
            print("Number {0} is already chosen or it's out of range.\n\
                  Please look at your board for available numbers.".format(choice))
#            self.plotBoard()
            return False
    
    def checkBoard(self):
        lines = 0
        y = self.board
        
        for row in self.board:
            if row.count("X") == 5:
                lines += 1
        for x in range(5):
            if (y[0][x],y[1][x],y[2][x],y[3][x],y[4][x]).count("X") == 5:
                lines += 1
        if (y[0][0],y[1][1],y[2][2],y[3][3],y[4][4]).count("X") == 5:
                lines += 1
        if (y[0][4],y[1][3],y[2][2],y[3][1],y[4][0]).count("X") == 5:
                lines += 1
        
        if lines >= 5:
            return True
        else:
            return False
        
       
            
        
        
        
        
        
        
        
            