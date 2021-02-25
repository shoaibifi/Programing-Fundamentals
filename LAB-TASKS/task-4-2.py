def unique_values(lis):
    unique_list=[]
    for i in lis:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
