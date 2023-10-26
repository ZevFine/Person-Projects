#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:11:22 2023

@author: zevfine
"""
import random
def reverse_madlib(filename):
    '''reads a text file or a madlib with the format (noun), (verb), ect'''
    #chooses either the pg or r dictionary 
    #d = rating
    fn = open(filename,'r')
    txt = fn.read()
    list = txt.split(' ')
    for i in range(len(list)):
        word = list[i]
        if word[0] == '(' and word[-1] == ')':
            part = word[1:-1]
            if part in pg:
                replacment = random.choice(pg[part])
                list[i] = replacment
    print(list)
    print(' '.join(list))
                
                
    
        
    
