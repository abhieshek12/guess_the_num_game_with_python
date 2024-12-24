num = int ( input("enter number of frinds"))
dic = {}
for i in range(num) :
    k =  ( input("enter name of frinds"))
    v =  ( input("enterfav lan of frinds"))
    dic.update({ k : v} ) 

print(dic.items)    