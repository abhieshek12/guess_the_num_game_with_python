f = open("srs.text" , "r") 

text = f.readline()

while (text != "") :
    print(text) 
    text = f.readline() 
f.close()    