## IMPORTS GO HERE
import os
## END OF IMPORTS

#### YOUR CODE FOR text_count FUNCTION GOES HERE ####
def text_count(directory,path,caps=False,char_count=False):
    file=[]
    filepath = os.path.join(directory,path)
    essay = open(filepath,"r")
    character_length=len(open(filepath,"r").read())
    for a in essay:
        strp = a.strip()
        file.append(strp.split(" "))
    output = 0
    if char_count == True:
        output= character_length
    elif caps == True:
        for b in file:
            for c in b:
                if not c =="":
                    if c.islower():
                        output+=1
    else:
        for x in file:
            for y in x:
                if not y =="":
                    output+=1
    essay.close()
    return output


#### End OF MARKER

#### YOUR CODE FOR copy_lines FUNCTION GOES HERE ####
def copy_lines(path_1,path_2,no_lines):
    path1 = open(path_1,"r")
    path2 = open(path_2,"w")
    file = []
    for i in path1:
        i = i.strip()
        if not i == "":
            file.append(i)
        else:
            file.append("\n")
            file.append(i)
    for j in range(0,no_lines):
        path2.write(file[j])
    path1.close()
    path2.close()

def copy_lines(input, output, a):
    
    
    
    
    with open("essay.txt","r") as z:
        with open("out.txt","w") as s:
            counter=0
            for i in z:
                counter+=1
                if a==1:
                    
                    data= i.strip()
                    s.write(data)
                    
                else:
                    
                    data=i
                    s.write(data)
                    
                    
                if counter==a:
                    break

#### End OF MARKER



