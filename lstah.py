
# its my first project in python 
import random as rd  

# game name is rock - paper - ceasor 
strs = ["rock" , "paper" , "ceasor"]
comp = rd.choice(strs) 
print("for \"rock\"-> r \n for \"paper\" -> p \n for \"ceasor\" -> c ")
player = input("enter your choice :").lower()

if comp == "rock" :
    if player == "r" : 
        print("its a draw")