# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:45:09 2018

@author: Pandora
"""

from bingo import Bingo
from user import User
from userBingo import CompPlayer
from realPlayer import RealPlayer
import time


class playGame(object):
    def __init__(self):
        self.welcome = "Welcome! You are going to play a Bingo!"
        print(self.welcome)
        self.playerTwo = User()
        self.playerOne = User()
#        self.turn == 0
        self.menu()
        
        
    def enterName(self):
        try:
            option = int(input("Would you like to type a name for %s?\n\
---Plese enter '1' for 'Yes' and '2' for 'N'.---\n"\
                             % ("yourself" if type(self.playerTwo) == CompPlayer else "you and your friend")))
        except ValueError:
            self.enterName()
        if option == 1:
            if type(self.playerTwo) == RealPlayer:
                self.playerOne.name = input("Please enter your name: ")
                self.playerTwo.name = input("Please enter your friend's name: ")
            else:
                self.playerOne.name = input("Please enter your name: ")
    
    def menu(self):
            try:
                option = int(input("Please type '1' if want to play against computer.\n\
Type '2' if prefer to play with a friend.\n\
My choice is: "))
            except ValueError:
                print("Please follow carefully the instructions. You didn't enter a number.")
                self.menu()
            if option not in (1,2):
                print("You typed a wrong number.")
                self.menu()
            else:
                if option == 1:
                    self.playerTwo = CompPlayer()
                    self.playerOne = RealPlayer()
                    
                else:
                    self.playerTwo = RealPlayer()
                    self.playerOne = RealPlayer()
                    self.playerTwo.name = "Player 2"
                self.enterName()
    
    def quitMessage(self):
        exit = None
        while exit not in ("q", "quit"):
            exit = input("Would you like to quit the game?\n\
To quit the game enter 'q' or write 'quit'\n\
For new game type 'N'.\nMy choice is: ")
            if exit.lower() == "n":
                p = playGame()
                p.game()
                time.sleep(10) 
            elif exit.lower() in ("q", "quit"):
                break
            else:
                print("Please make sure that you typed a proper character")
                self.quitMessage()
    
    
    
    
    
    def game(self):
        while self.playerOne.checkBoard() == False and self.playerTwo.checkBoard() == False:
            
            print("%s's board:\n"%(self.playerOne.name)), self.playerOne.plotBoard()
            
            self.playerOne.updateBoard(self.playerOne.messageChoice())
            self.playerTwo.updateBoard(self.playerOne.choice)
            if self.playerTwo.checkBoard() == True:
                break
            
            if type(self.playerTwo) == RealPlayer:
                print("%s's board:\n"%(self.playerTwo.name)), self.playerTwo.plotBoard()
                self.playerTwo.updateBoard(self.playerTwo.messageChoice())
                self.playerOne.updateBoard(self.playerTwo.choice)
            else:
                self.playerTwo.updateBoard(self.playerTwo.choose())
                print("\n----------\nYour opponent's choice is {0}.\n\
                      --------------".format(self.playerTwo.choice))
                self.playerOne.updateBoard(self.playerTwo.choice)
        
        if self.playerOne.checkBoard() == True and self.playerTwo.checkBoard() == True:
            print("Bingo! \n---Standoff---\n\n")
            self.quitMessage()
        elif self.playerOne.checkBoard() == True:
            print("Bingo!\n\
                  Congratulations %s\n\n"%(self.playerOne.name))
            self.quitMessage()
        else:
            print("Bingo!\n\
                  Congratulations %s\n\n"%(self.playerTwo.name))
            self.quitMessage()
            



p = playGame()
p.game()
time.sleep(10)            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        