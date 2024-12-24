 
import random 

print(" in this game computer will genrate random no. between 1 and 100 and you have to choose .. lets start ..")
num = random.randrange(1,101)
print("computer has genrated a number guess it the number is between 1 and 100 ")
score = 1 

inp = int(input("give your input  : "))
 
while num != inp :
     if abs(num - inp) < 5 :
         print("very close to it ")
         if inp < num :
            print(f" the number genrated by computer is greater then {inp}")    
         else :
            print(f" the number genrated by computer is less then {inp}")  
         
     elif inp < num :
         print(f" the number genrated by computer is greater then {inp}")    
     else :
          print(f" the number genrated by computer is less then {inp}")    
     score += 1   
     inp = int(input("give your input again  : "))
print(f" yess you guess correct the number  is {num} your score is {score}")     