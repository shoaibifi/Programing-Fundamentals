### qno3
def returnGreaterSum(nestedlist):
    sg = 0                 
    ind = 0
    for i in a:   # loop on list  means i =  [1,2,4], i = [8,5,4] i = [1,1,2,3]
        s1 = 0
        for j in i: # loop on i means  j = 1,j=2,j=4------ j=8.j=5,j=4,--------- j=1,j=1,j=2,j=3
            s1+=j    # it will sum the inner list 
        if s1 > sg:  # here we are storing the greater sum
            sg  = s1
            ind = nestedlist.index(i)   # here we are storig the index of list whose sum is greater..........
    return(nestedlist[ind])


a = [[1,2,4], [8,5,4], [1,1,2,3]]
returnGreaterSum(a)
