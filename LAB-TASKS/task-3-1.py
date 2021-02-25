for i in range(1,6):  # we have got five row in question so we run loop five times
    for j in range(1,6-i):    # we have to adjust spaces according to the question so in first line there are 4 apaces and star so we will sbtract the number of rows that we want to print from first loop 
        print(" ",end="")      # here we are printing spaces and we are using (end) its a built in function that will prints the values of loop in one line 
    for k in range(1,i+1):    # here we are runing the loop upto the first loop its a nested loop 
        print("*",end="")     # here it will print stars and remember one thing it will print star with spaces because we are using (end) on both loops 
    print("\n")               # here we are wanting to change the line when the value of i changes
