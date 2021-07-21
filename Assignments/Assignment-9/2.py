#Qno:2
while True:       
    c = 0
    l = []
    u = []
    import random 
    while c<5:
        n = random.randint(1,40) 
        l.append(n)
        c+=1


    def fun(lis):
            cr=0
            lis.sort()
            for i in range(0,5):
                print("\nEnter the",i+1,"integer:",end="")
                a = int(input())
                u.append(a)

            for i in range(len(l)):
                if l[i]==u[i]:
                    cr+=1
            if cr==len(l):
                print("‘‘You win!’’ ")
            else :
                print("‘‘You lose!’’\nLottery number: ",end="")
                for i in l:
                    print(i,end="")
   
    fun(l)
    a = input("\nContinue y/n: ")
    if a=="n" or a=="N":
        break

