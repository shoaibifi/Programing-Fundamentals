import os
file_name = os.path.join("Desktop","names.txt")  
with open(file_name,"r") as f:
    for i in f:
        print(i[-4:].strip())  # here -4 means it will start printing letters from 4th positon and strip function is used for remove \n 
