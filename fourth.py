class employ :
    lang = "java" 
    company_Name = "laura"
    sal = 900 
    def __init__(self , nme ,pst ,  sal = 900 ):
        self.name = nme 
        self.post = pst 
        self.sal = sal 
        print("created object ")
        
e1 = employ("abhi" , "hr" , 1999)
e1.size = 99         
print(e1.name , e1.company_Name , e1.post , e1.sal , e1.size) 
