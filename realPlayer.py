# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:45:54 2018

@author: Pandora
"""

import random
from user import User

class RealPlayer(User):
    def __init__(self):
        User.__init__(self)
        self.name = "Player 1"

    
    def messageChoice(self):
        try:
            self.choice = int(input("Please choose a number from your board.\n\
My choice is: "))
        except (ValueError, TypeError):
            print("You didn't enter a proper number. Make sure that your choice\n\
is in range of 1 to 25 and it is still on the board.")
            self.messageChoice()
        if self.choice in self.numbers:
                return self.choice
        else:
            print("Make sure that your choice is in range of 1 to 25 and it is still on the board.")
            self.messageChoice()
