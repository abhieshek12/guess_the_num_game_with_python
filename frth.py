import os 



a =  "\\my java"
 
if (os.path.exists(a)) :
    cont = os.listdir(a) 
    print(cont)
else :
    print(f"the directory {a} does not exist ")    