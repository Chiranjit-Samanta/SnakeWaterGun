# -*- coding: utf-8 -*-
"""MY FIRST GAME

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ibQkCY-Gf75cne5XO0POiZONhnI__L3t
"""

# 1 GAME DEVELOPED BY ME
# GAME NAME IS SNAKE(S), WATER(W) & GUN(G)

import random
def gamewin(computer, you):
  if computer == you:
    return None

  elif computer =="S":
    if you == "W":
      return False
    elif you =="G":
      return True

  elif computer == "W":
    if you == "G":
      return False
    elif you == "S":
      return True

  elif computer == "G":
    if you == "S":
      return False
    elif you == "W":
      return True

print ("Computer Turn: SNAKE(S), WATER(W) & GUN(G)")
rand_no = random.randint(1,3)
if rand_no == 1:
  computer = "S"
elif rand_no == 2:
  computer = "W"
else:
  computer = "G"

you = input ("Your Turn: SNAKE(S), WATER(W) & GUN(G)")
a = gamewin(computer,you)

print(f"Computer Choosen {computer}")
print(f"You Choosen {you}")

if a== None:
  print("The Game Is Tie!")
elif a:
  print("You Won!")
else:
  print("You Lose!")