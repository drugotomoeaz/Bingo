# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:21:50 2018

@author: Pandora
"""

from user import User
import random


class CompPlayer(User):
    def __init__(self):
         User.__init__(self)
         self.name = "Gosho"
         
    def choose(self):
        choiceRate = {}
        
        if self.time == 0:
            y = self.numbers[:5:4] + [self.numbers[12]] + self.numbers[20:25:4]
            if "X" in y:
                y.remove("X")
            self.choice = random.choice(y)
            self.time += 1
            return self.choice
        else:
            for x in range(5):
                #rate of every row on the board
                choiceRate[self.numbers[5*x:5*(x + 1)].count("X")] = self.numbers[5*x:5*(x + 1)]
                #rate of every column on the board
                choiceRate[self.numbers[x::5].count("X")] = self.numbers[x::5]
            
            #rate of every diagonal on the board
            choiceRate[self.numbers[::6].count("X")] = self.numbers[::6]
            choiceRate[self.numbers[4::5].count("X")] = self.numbers[4::5]
        
        if 5 in choiceRate:
            del choiceRate[5]
        self.choice = choiceRate[max(choiceRate)]
        for x in range(max(choiceRate)):
            self.choice.remove("X")
        
        self.choice = random.choice(self.choice)
        self.time += 1
        return self.choice

#p = CompPlayer()
#p.plotBoard()
##print(p.choose())
#p.updateBoard(p.choose())
