names_file = open(filename, "r")
shortest_names = [] # List of shortest names. Right now it's empty.
for l in names_file:
    if len(shortest_names) == 0: 
        shortest_names = [l]
    else:
        
        if len(l) < len(shortest_names[0]): # No! This name is shorter!
            shortest_names = [l]
        else:
            if len(l) == len(shortest_names[0]): # This name is the same length.
                shortest_names.append(l) # It gets to join the list.
        # In any other case, the name must be longer than ones in the list.
names_file.close()
# Print the names:
for n in shortest_names:
    print n
