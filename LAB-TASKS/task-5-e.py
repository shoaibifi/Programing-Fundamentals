def fun():
    import os
    names_list = []
    file_name = os.path.join("Desktop","names.txt")
    with open(file_name,"r") as f:
        for i in f:
            names_list.append(i.strip())
        a = input("Enter the name ")
        if a in names_list:
            return True
        else:
            return False
        
        
