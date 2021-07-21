# Qno-1
a = [1,2,2,3,4,9]
n = 0
l = []
while n<len(a):  # here we are making sure that looop runs upto the 
    counter=0    # this counter is for to count the each number how many times enterd and will become zero for next number
    s = a[n]     # here we are taking the first number of the list
    n+=1         # and here we are adding one in n on each iteration so it compares the every number of list 
    if s in l:  # and if we have checked the number previously now no need to to check again.
        continue
    else:         
        for i in a:  # loop on given list
            if s==i:
                counter+=1
                l.append(s) # we are appending the number that we checked, in a new list because we dont want to check it again
        print(s,"occurred",counter,"times")
    
