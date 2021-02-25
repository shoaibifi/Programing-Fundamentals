import os            # 
name_list=[]
file_name = os.path.join("Desktop","names.txt")
with open(file_name,"r") as f:
    for line in f:
        name_list.append(line.strip())
file=os.path.join("Desktop","name_roll.txt")
with open(file,"w") as m:
    for i in name_list:
        a=input("Enter the Roll no for "+i+" ")
        m.write("\n"+i+" "+a)
        
        
        
