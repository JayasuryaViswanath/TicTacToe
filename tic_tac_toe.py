# -*- coding: utf-8 -*-
"""Tic Tac Toe

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k_Bd0FMUrQ3Ko1GPacW2uSq-ZIgkofA1
"""

#samplelist

list1 = ['','O','']

from random import shuffle

def shuffling(new_list):

  shuffle(new_list)

  return new_list

shuffled_list = shuffling(list1)

#print(shuffling(list1))

#guessing

def player_guess():

  guess = ' '

  while guess not in ['0','1','2']:

    guess = input('Enter any number in 0 1 or 2  : ')

  return int(guess)

#checking 

guess = player_guess()

def checking(lissy,guess):

  if lissy[guess] == 'O':

    print('Your guess is right')
  else:

    print('Your guess is wrong')
    print(lissy)

checking(shuffled_list,guess)