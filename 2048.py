#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:18:50 2023

@author: zevfine
"""

import random
class Board:
    
    def __init__(self):
        #self.board = [['    '] * 4 for row in range(4)]
        self.board = [['    '] * 4 for row in range(4)]
        self.merged = [[False] * 4 for row in range(4)]
    
    
    def __repr__(self):
        a = 21 * '-' + '\n'
        s = ''
        s += a
        for row in range(4):
            s +='|'
            for col in range(4):
                s += self.board[row][col] + '|'
            s += '\n'
            s += a
        return s 
    
    def move_down(self):
        '''moves each row down until it either cannot 
        move down more or merges... each square can only merge once'''
        for row in range(3):
            for col in range(4):
                for i in range(3):
                    if self.board[3-i][col] == '    ':
                        self.board[3-i][col] = self.board[3-i-1][col]  
                        self.board[3-i-1][col] = '    '
                    if self.board[3-i][col] == self.board[3-i-1][col] and self.board[3-i][col] != '    ':
                        if self.merged[3-i][col] == False and self.merged[3-i-1][col] == False:
                            self.board[3-i][col] = (4-len(str(int(self.board[3-i-1][col].strip())*2))) * ' ' + str(int(self.board[3-i-1][col].strip())*2)
                            self.board[3-i-1][col] = '    '
                            self.merged[3-i][col] = True
        for row in range(4):
            for col in range(4):
                self.merged[row][col] = False
    
    def move_up(self):
        '''moves each row up until it either cannot 
        move up more or merges... each square can only merge once'''
        for row in range(3):
            for col in range(4):
                for i in range(3):
                    if self.board[i][col] == '    ':
                        self.board[i][col] = self.board[i+1][col]
                        self.board[i+1][col] = '    '
                    if self.board[i][col] == self.board[i+1][col] and self.board[i][col] != '    ':
                        if self.merged[i][col] == False and self.merged[i+1][col == False]:
                            self.board[i][col] = (4-len(str(int(self.board[i+1][col].strip())*2))) * ' ' + str(int(self.board[i+1][col].strip())*2)
                            self.board[i+1][col] = '    '
                            self.merged[i][col] = True
        for row in range(4):
            for col in range(4):
                self.merged[row][col] = False
            
    def move_right(self):
        '''moves each row right until it either cannot 
        move down more or merges... each square can only merge once'''
        for row in range(4):
            for col in range(3):
                for i in range(3):
                    if self.board[row][3-i] == '    ':
                        self.board[row][3-i] = self.board[row][3-i-1]
                        self.board[row][3-i-1] = '    '
                    elif self.board[row][3-i] == self.board[row][3-i-1] and self.board[row][3-i-1] != '    ':
                        if self.merged[row][3-i-1] == False and self.merged[row][3-i] == False:
                            self.board[row][3-i] = (4-len(str(int(self.board[row][3-i].strip())*2))) * ' ' + str(int(self.board[row][3-i].strip())*2)
                            self.board[row][3-i-1] = '    '
                            self.merged[row][3-i] = True
        for row in range(4):
            for col in range(4):
                self.merged[row][col] = False
    
    def move_left(self):
        '''moves each row right until it either cannot 
        move down more or merges... each square can only merge once'''
        for row in range(4):
            for col in range(3):
                for i in range(3):
                    if self.board[row][i] == '    ':
                        self.board[row][i] = self.board[row][i+1]
                        self.board[row][i+1] = '    '
                    elif self.board[row][i] == self.board[row][i+1] and self.board[row][i+1] != '    ':
                        if self.merged[row][i] == False and self.merged[row][i+1] == False:
                            self.board[row][i] = (4-len(str(int(self.board[row][i].strip())*2))) * ' ' + str(int(self.board[row][i].strip())*2)
                            self.board[row][i+1] = '    '
                            self.merged[row][i] = True
        for row in range(4):
            for col in range(4):
                self.merged[row][col] = False
                
    def add_new_numbers(self):
        '''adds new numbers to the board either a two a ten percent chance of 4'''
        countera = 0
        break_out = False
        #counter to see if there are more than one empty space
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == '    ':
                    countera += 1
                if countera == 2:
                    break_out = True
                    break
            if break_out == True:
                break
        if countera == 1:
            counterb = 1
        else:
            counterb = 0
        #counterb is for the while loop 
        next_number = ''
        while counterb != 2:
            chance = random.randint(1,10)
            if chance == 10:
                next_number = '   4'
            else:
                next_number = '   2'
            row = random.randrange(0, 4)
            col = random.randrange(0, 4)
            if self.board[row][col] == '    ':
                self.board[row][col] = next_number
                counterb += 1
                
    def can_move_down(self):
        '''checks if player can move down'''
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row+1][col]:
                    return True
                if self.board[row+1][col] =='    ' and self.board[row][col] != '    ':
                    return True
        return False 
    
    def can_move_up(self):
        '''checks if player can move up'''
        for row in range(3):
            for col in range(4):
                if self.board[3-row][col] == self.board[3-row-1][col]:
                    return True
                if self.board[3-row-1][col] =='    '  and self.board[3-row][col] != '    ':
                        return True
        return False
    
    def can_move_left(self):
        '''checks if player can move left'''
        for row in range(4):
            for col in range(3):
                if self.board[row][col] == self.board[row][col+1]:
                    return True
                if self.board[row][col] =='    ' and self.board[row][col+1] != '    ':
                        return True
        return False
    
    def can_move_right(self):
        '''checks if player can move right'''
        for row in range(4):
            for col in range(3):
                if self.board[row][col] == self.board[row][col+1]:
                    return True
                if self.board[row][col] =='    ' and self.board[row][col+1] != '    ':
                    return True
        return False
    
    def can_move(self):
        '''runs all can_move methods for the game over condition'''
        if self.can_move_down() != True\
            and self.can_move_up() != True\
                and self.can_move_right() != True\
                    and self.can_move_left() != True:
                        return False
    
    def is_win(self):
        '''checks if player has reached 2048'''
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == '2048':
                    return True
        return False 
        
                
def run_game():
    '''runs 2048'''
    b = Board()
    b.add_new_numbers()
    print(b)
    while True:
        print('1-up,2-down,3-left,4-right')
        move = int(input('Enter Move: '))
        if move == 1:
            if b.can_move_up() == True:
                b.move_up()
            else:
                print('Invalid Move')
                continue
        elif move == 2:
            if b.can_move_down() == True:
                b.move_down()
            else:
                print('Invalid Move')
                continue
        elif move == 3:
            if b.can_move_left() == True:
                b.move_left()
            else:
                print('Invalid Move')
                continue
        elif move == 4:
            if b.can_move_right() == True:
                b.move_right()
            else:
                print('Invalid Move')
                continue
        else:
            print('Please Enter Valid Move')
            continue
        if b.is_win() == True:
            print("Conragulations!!! You've Reached 2048!!!")
        b.add_new_numbers()
        print(b)
        if b.can_move() == False:
            print('Game Over')
            break
run_game()
        
        
        