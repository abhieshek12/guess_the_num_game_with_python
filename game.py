import random 
while True :
    a = input(" you want to play .. yes or no ")
    if a == "no" :
        with open("high_score.txt","w+") as s :
            if s.read == "" :
                print("no score play once plz  ")
            else :
                print( "score is " , s.read())
                s.close()
        break 
    elif a == "yes" :
        score = random.randint(1,1000) 
        with open("high_score.txt", "w+" ) as s :
            sr = s.read()
            if sr == "" : 
                s.write(score)
            elif score > int(sr):
                s.write(score)
            s.close()
    else : 
        print("give valid input asshole")
                
                
