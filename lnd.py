# class employ :
 
#     def __init__(l):
#         print("i am super ")
#     @staticmethod    
#     def show () :
#         print("i am super method ")   

# class em (employ) :
    
#     def __init__(l):
#        print("i am sub ")
#     @staticmethod
#     def show () :
#         print("i am sub method ")  
        
        
# a = employ()        
# a.show()

# b = em()
# super(em , b).show()

# a = [1 , 2 , "ramesh "]
# b = a[0] 
# c = a[2]
# print( type(a) , type(b) , type(c))

# a = " am name is abhishek "
# b = a.split( " ")
# print(b )
# print(type(b))

# class emp :
#     @classmethod 
#     @staticmethod
#     def func() :
#         print("i am a class method")
        
        
        
# emp.func()        

# class human :

#     def __init__(self , name ):
#         self.firstName = name.split(" ")[0]
#         self.lastName = name.split(" ")[1]
#     @property
#     def get (self) :
#         return self.firstName + "\t" +self.lastName 
    
#     def __str__(self):
#         return self.firstName + "\t" +self.lastName  
    
# h1 = human("abhishek malviya")    

# b = str(h1)

# print(b)

# class vector :
#     def __init__(self , x ,y , z ):
#         self.x = x 
#         self.y = y 
#         self.z = z 
        
#     def __str__(self ) :
#         return f" vector : {self.x}x + {self.y}y + {self.z}z" 
    
    
#     def __add__(self , vec) :
#         res  = vector(self.x + vec.x , vec.y + self.y , self.z + vec.z)
#         return res 
        
        
        
# v1 = vector(2,3,4)   
# v2 = vector(4,5,6)
# v3 = v2 + v1
# print(v3)

# a = input("enter a no. :")
# b = input("enter a no. : ")

# if b == 0 :
#     raise ZeroDivisio  

# else :
#     print (a//b)

# a = 89

# def fun(): 
     
#     a = 3
    


# fun()
# print(a)

# square = lambda x : x*x 

# b = square(5)
# print(b)

# sum = lambda a , b , c : a+b+c 

# print(sum(2,4,4))

l : list[int] = ["ch" , "u" , "ti" , "ya"]
# lst = map(square , l )
# ls = list(lst)
# print(type(lst) , type(ls) , ls)

# def even(n) :
#     if (n%2==0) :
#         return True
#     else :
#         False 
# onev =  filter(even, ls)       
# print( type(onev) , list(onev))       
# from functools import reduce 
# mul = lambda a,b:a*b 

# # print(reduce(mul , l ))

# st = "  ".join(l)
 
# # print(st , type(st))

# list = [i*7 for i in range(1,11)]

# txt = " "
# for i in list :
#     txt += f" {i}  \n"
    
    
# print(txt)    
# 5,6,9,10,89,100
lis = [5,6,9,10,89,100]

def div_by_five(n) :
    if n %5 == 0 :
        return True
    else: 
        return False 

print(list(filter(div_by_five , lis)))
