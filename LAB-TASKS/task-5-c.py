names_list=[]
len_list= []
summ=0
import os
file_name = os.path.join("Desktop","names.txt")
with open(file_name,"r") as f:   # were have opened the file in read mode
    for line in f:               # here we are running a loop on file which contains the name which is at desktop
        names_list.append(line.strip()) #  we are appending the names in list because we have to calculate the length of single  
    for i in names_list:                # here we are running a loop on names list 
        len_list.append(len(i))         # here we are appending the lenghth of a single name  on each iteration in a list
    for j in len_list:                   # we are just calculating the sum of the lengths of the name
        summ+=j
print(summ)
        
        
