dic = {
    "help" : "मदद" ,
    "poet" : "कवि" , 
    "paper" : "कागज"
}

a = input("enter a word  :")
b = a.lower()
print(f"the hindi meaning of {a}  is { dic.get(b)}") 