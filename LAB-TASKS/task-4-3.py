def sorted_list(lis):
    for i in range(0,len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i]>lis[j]:
                lis[i],lis[j]=lis[j],lis[i]
    return lis
        
