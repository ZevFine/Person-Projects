#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:01:56 2023

@author: zevfine
"""
import random
from tttboard import *
from humanplayer import *

def ttt():
    """ plays the game of tic tac toe 
    """

    p1 = Player("X")
    p2 = Player("O")
    if p1.marker not in 'XO' or p2.marker not in 'XO' \
       or p1.marker == p2.marker:
        print('need one X player and one O player.')
        return None

    print('Welcome to TIC TAC TOE!')
    print()
    print("Is three in a row a win or a loss?")
    answer = str(input('Enter asnwer:'))
    b = board()
    if answer == "win":
        print(b)
        while True:
            if process_move(p1, b,p2) == True:
                return b        
            if process_move(p2, b,p1) == True:
                return b
    else:
        p1 = ThreePlayer("X")
        p2 = ThreePlayer("O")
        b = ThreeBoard()
        print(b)
        while True:
            if process_movel_three(p1, b, p2) == True:
                return b
            if process_movel_three(p2, b, p2) == True:
                return b
            
def process_move(p, b, p2):
    '''takes user input and adds it to the board'''
    print(p, "'s turn")
    while True:
        move = p.next_move(b)
        if b.can_add_to(move[0], move[1]) == True :
            break
        print('cannot add to' , move[1] , ',' , move[0])
        print()
        print('please try again')
    b.add_marker(move[0], move[1], p.marker)
    print()
    print(b)
    if b.is_win_for(p.marker) == True:
       # print(p, "wins in", p.num_moves, 'moves')
        print("Congratulations")
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False


def process_movel_three(p, b, p2):
    '''takes user input and adds it to the board'''
    print(p, "'s turn")
    while True:
        move = p.next_move(b)
        if b.can_add_to(move[1], move[2], move[0]) == True:
            break
        print('cannot add to' , move[2] , ',' , move[1])
        print()
        print('please try again')
    b.add_marker(move[1], move[2],p.marker,move[0])
    print()
    print(b)
    if b.is_win_for(p.marker) == True:
       # print(p.opponent_marker(), "wins in", p2.num_moves, 'moves')
        print("Congratulations")
        return True
    elif b.is_full([move[0]]) == True:
        print("It's a tie!")
        return True
    else:
        return False

   

    
    
    

    
            
                
    


