#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:56:03 2023

@author: zevfine
"""

def madlib(filename):
    '''reads a madlib and asks for the inputs'''
    fn = open(filename,'r')
    txt = fn.read()
    word_list = txt.split(' ')
    print(word_list)
    for i in range(len(word_list)):
        word = word_list[i]
        if '(' in word:
            print(word)
        front = False
        back = False
        if word[0] == '(':
            part = word[1:-1]
            if '_' in part:
                part = part.replace("_", ' ')
            if part[0] in 'aeiou':
                replacment = str(input('Enter an ' + str(part) + ':'))
            else:
                replacment = str(input('Enter a ' + str(part) + ':'))
            word_list[i] = replacment
    string = (' '.join(list))
    return string