# qno 2 with other logic

#Qno:2
choice = "y"
while choice =="y" or choice == "Y":       
    l = []
    u = []
    import random 
    for i in range(0,5):
        n = random.randint(1,40)
        l.append(n)


    def fun(lis):
        lis.sort()
        randomsum = 0
        usersum = 0
        
        for i in lis:
            randomsum+=i
        
        
        for i in range(0,5):
            print("\nEnter the",i+1,"integer:",end="")
            a = int(input())
            u.append(a)
        
        for j in u:
            usersum+=j
            
            
        if randomsum==usersum:
            print("‘‘You win!’’ ")
        else :
            print("‘‘You lose!’’\nLottery number: ",end="")
            for i in l:
                print(i,end="")
   
    fun(l)
    choice = input("\nContinue y/n: ")
   

