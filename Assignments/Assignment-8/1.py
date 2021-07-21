
def divisor(n,b):
    if b == True:
        for i in range(1,n):
            if n%i == 0:
                if i%2==0:
                    print(i)
    else :
        for i in range(1,n):
            if n%i == 0:
                if not i%2==0:
                    print(i)
    
    
