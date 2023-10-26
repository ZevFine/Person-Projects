#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:40:58 2023

@author: zevfine
"""
from tttboard import *
class Player():
    def __init__(self, marker):
        '''is constructor for Player'''
        assert (marker == "X" or marker == "O")
        self.marker = marker
        self.num_moves = 0
        
    def __repr__(self):
        '''string representation of player'''
        return "player" + self.marker

    
    def opponent_marker(self):
        '''shows other if other player is X or O'''
        if self.marker == "X":
            return "O"
        else:
            return "X"
        
    def next_move(self,b):
        '''gets the next move by collecting the row and col and putting them in a list'''
        list = []
        while True:
            row = int(input('Enter a row: '))
            if row in range(3):
                list += [row]
                col = int(input('Enter a col: '))
                if col in range(3):
                    list +=[col]
                    break
                else:
                    print("Try again!")
                    print()
            else:
                print("Try again!")
                print()
        self.num_moves += 1
        return list
            
    
class ThreePlayer(Player):
    def __init__(self, marker):
        '''is constructor for Player'''
        assert (marker == "X" or marker == "O")
        self.marker = marker
        self.num_moves = 0
        
    def __repr__(self):
        '''string representation of player'''
        return "player" + self.marker

    
    def opponent_marker(self):
        '''shows other if other player is X or O'''
        if self.marker == "X":
            return "O"
        else:
            return "X"
    def next_move(self,b):
        list = []
        while True:
            board = int(input('Enter a board: '))
            if board in range(3):
                list += [board]
                row = int(input('Enter a row: '))
                if row in range(3):
                    list += [row]
                    col = int(input('Enter a col: '))
                    if col in range(3):
                        list +=[col]
                        break
                    else:
                        print("Try again!")
                        print()
                else:
                    print("Try again!")
                    print()
            else:
                print("Try Again!")
                print()
        return list
