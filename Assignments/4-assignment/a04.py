### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def openLocks(number_of_lockers,number_of_students):
 
    if number_of_lockers < 0:
        return None
    if  number_of_students < 0:
        return None
    
    if number_of_lockers == 0: 
        return 0
    if  number_of_students == 0:
        return 0
 
    lis= []
    
    for i in range (number_of_lockers):
        lis.append(0)

    locks = 0
    for i in range (0,number_of_students):
        if i == 0:
            for j in range (0,number_of_lockers):
                lis[j] = 1
        elif i == 1:
            for j in range (0,number_of_lockers):
                if j%2==1:
                    lis[j] = 0
        else:
            for j in range (i,number_of_lockers,i+1):
                if lis[j]==1:
                    lis[j]=0
                else:
                    lis[j]=1
    for i in range (0,number_of_lockers):
        if lis[i]==1:
            locks = locks + 1
    return locks


#### End OF MARKER





### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
def mostTouchableLocker(number_of_lockers,number_of_students):
    
    if number_of_lockers < 0:
        return None
    if  number_of_students < 0:
        return None
    
    if number_of_lockers == 0: 
        return 0
    if  number_of_students == 0:
        return 0
   
    lis= []
    
    for i in range (number_of_lockers):
        lis.append(0)

    max_ = 0
    for i in range (0,number_of_students):
        if i == 0:
            for j in range (0,number_of_lockers):
                lis[j] = 1
        elif i == 1:
            for j in range (0,number_of_lockers):
                if j%2==1:
                    lis[j] = lis[j] + 1
        else:
            for j in range (i,number_of_lockers,i+1):
                lis[j]= lis[j] + 1
 
    most = 0
    for i in range (0,number_of_lockers):
        if lis[i] >= max_:
            max_ = lis[i]
            most = i+1
    
 
    return most
#### End OF MARKER


