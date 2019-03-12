#sayısal tahmin oyunu
while True:
    lottery=[]
    myguess=[]
    from random import randint
    while len(lottery)<6:               
        x=randint(1,49)
        if x in lottery:    
            continue        
        lottery.append(x)
    while len(myguess)<6:             
        guess=int(input("(1-49) write a number"))
        if guess in myguess or guess<0 or guess>49:     
            print("try again")                                       
            continue                                                 
        myguess.append(guess)
    youfound=0
    foundthese=[]
    for k in myguess:
        for j in lottery:
            if j==k:
               youfound+=1
               foundthese.append(k)
    lottery.sort()        
    print("Results: ",lottery)
    myguess.sort()
    print("Guesses:",myguess)
    print("you found:",youfound,"They are:",foundthese)
    
    
    
