# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:27:44 2018

@author: Pandora
"""


from bingo import Bingo

class User(Bingo):
    def __init__(self):
        Bingo.__init__(self)
        self.name = None
        self.time = 0
        self.choice = None