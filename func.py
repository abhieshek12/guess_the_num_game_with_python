# def sum (n) :
#     if n < 0 :
#         print("give positive no.")
#         return 
#     if n == 0 : 
#         return 0 
#     if n == 1 :
#         return 1 
#     return n + sum(n-1) 




# def prnt_pattern (n) :
#     if n == 0 :
#         return 
#     print( "*" * n )
#     prnt_pattern(n-1)


# prnt_pattern(4)

# a = "abhishek"
# b = a.strip("ek")
# print(b)

# def mult_table(n) :
#     mul(n , 1)
    
    
# def mul(n , i ) :
#     if i == 11 :
#         return 
#     print(f"{n} X {i} = {n*i}")
#     mul(n , i + 1)
      
      
# mult_table(6)      
    
with open("srs.text") as pm :
    lines= pm.readlines()
    
    for item in lines :
        if "harry" in item :
            print("yess")
            print(type(item))
            break 
    else :
        print("no")