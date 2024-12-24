a = int(input("enter marks "))
c = int(input("enter marks "))
d = int(input("enter marks "))
if (a < 33) :
    print("fail")

elif (c < 33) :
    print("fail")
    
elif (d < 33) :
    print("fail")
elif (((a + c + d ) / 300 ) * 100) < 40 :
    print("fail")       
else :
    print("pass")    