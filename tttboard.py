#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:39:18 2023

@author: zevfine
"""

class board():
    def __init__(self):
        '''constructor for the board'''
        self = self
        self.slots = [[' '] * 3 for row in range(3)]
  
    def __repr__(self):
        '''creates a string representation of the board'''
        s = ''
        a = " " + '-' * 7 + '\n'
        s += a
        for row in range(3):
            s += str(row) + '|'
            for col in range(3):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += a
        s += '  0 1 2'
        return s
    
    def add_marker(self, row, col, marker):
        '''adds a marker to the board'''
        #assertions to make sure everything is Kosher
        assert (col in range(3)\
                and row in range(3)\
                    and marker == "X" or marker == "O")
        self.slots[row][col] = marker
   
    def is_win_for(self,marker):
        '''runs all of the win checkers'''
        print('hefadgfaddfadfajdsfl;adlfkadkflkggaysex')
        if self.is_win_d(marker) == True\
            or self.is_win_h(marker) == True\
                or self.is_win_v(marker) == True:
                    return True
    
        
    def is_win_d(self, marker):
        '''checks diagnal for win'''
        if self.slots[1][1] == marker:
            if self.slots[0][0] == marker and self.slots[2][2] == marker:
                return True 
            elif self.slots[0][2] == marker and self.slots[2][0] == marker:
                return True 
        
    def is_win_h(self,marker):
        '''checks for horizontal win'''
        for i in range(3):
            if self.slots[i][0] == marker\
                and self.slots[i][1] == marker\
                    and self.slots[i][2] == marker:
                        return True
                    

    def is_win_v(self, marker):
        '''checks for a vertical win'''
        for i in range(3):
            if self.slots[0][i] == marker and self.slots[1][i] == marker\
                and self.slots[2][i] == marker:
                    return True
        
    def reset(self):
        '''resets the board'''
        self.slots = [[' '] * 3 for row in range(3)]
        
    def can_add_to(self, row, col):
        '''checks if player can play in the column'''
        if row < 0 or row > 2 or col > 2 or col < 0:
            return False
        if self.slots[row][col] != ' ':
            return False
        else:
            return True 
       
    def is_full(self):
        '''checks if the baord is full'''
        for i in range(3):
            for j in range(3):
                if self.can_add_to(i, j) == True:
                    return False
        return True
    
    def remove_marker(self, col,row):
        '''removes the checker on the top of the column'''
        if self.slots[row][col] != ' ':
            self.slots[row][col] = ' '

class ThreeBoard(board):
    
    def __init__(self):
        self = self
        #creating three different boards so we can edit one with out affecting others
        self.slots0 = [[' '] * 3 for row in range(3)]
        self.slots1 = [[' '] * 3 for row in range(3)]
        self.slots2 = [[' '] * 3 for row in range(3)]
        self.thr = [self.slots0] + [self.slots1] + [self.slots2]
        
    def __repr__(self):
        '''creates a string representation of the board'''
        s = ''
        for i in range(3):
            s += ' Board' + str(i) +'\n'
            a = " " + '-' * 7 + '\n'
            s += a
            for row in range(3):
                s += str(row) + '|'
                for col in range(3):
                    s += self.thr[i][row][col] + '|' 
                s += '\n'
            s += a
            s += '  0 1 2 \n'
        return s
              
   
    def add_marker(self, row, col, marker, b):
        '''adds a marker to the board'''
        assert (col in range(3))
        assert (row in range(3))
        assert (marker == "X" or marker == "O")
        self.thr[b][row][col] = marker
   
    def reset(self):
        '''resets the board'''
        self.slots = [[' '] * 3 for row in range(3)]
        
    def can_add_to(self, row, col,b):
        '''checks if player can play in the column'''
        if type(b) == list: #when checking the is tie for process move b was a list not a int
            b = b[0]
        if row not in range(3) or col not in range(3):
            return False
        if self.thr[b][row][col] != ' ':
            return False
        else:
            return True 
       
    def is_full(self,board):
        '''checks if the baord is full'''
        for i in range(3):
            for j in range(3):
                if self.can_add_to(i, j,board) == True:
                    return False
        return True
    
    def remove_checker(self, col, row, b):
        '''removes the marker'''
        if self.slots3[b][row][col] != ' ':
            self.slots3[b][row][col] = ' '
    def is_win_d(self, marker):
        '''checks diagnal for win'''
        for i in range (3):
            if self.thr[i][1][1] == marker:
                if self.thr[i][0][0] == marker and self.thr[i][2][2] == marker:
                    return True 
                elif self.thr[i][0][2] == marker and self.thr[i][2][0] == marker:
                    return True 
        
    def is_win_h(self,marker):
        '''checks for horizontal win'''
        for j in range(3):
            for i in range(3):
                if self.thr[j][i][0] == marker\
                    and self.thr[j][i][1] == marker\
                        and self.thr[j][i][2] == marker:
                        return True

                    

    def is_win_v(self, marker):
        '''checks for a vertical win'''
        for j in range(3):
            for i in range(3):
                if self.thr[j][0][i] == marker\
                    and self.thr[j][1][i] == marker\
                        and self.thr[j][2][i] == marker:
                        return True