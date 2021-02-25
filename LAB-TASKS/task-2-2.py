while True: # it will run run the program until we select No 
    a=int(input("Enter the real number")) # asking a number from user
    b=str(a)   # here we are doing type casting because we are wanting to run a loop on a number that we have got from the user and append it in  a list and we know tha we cant use loop on integer that's why we are doing type casting 
    lis=[]
    sum1=0
    for i in b: # loop on number that we got from user
        lis.append(int(i))  # here we are againg doing type casting, we are appending the number in a list in the form of integers because we are wanting to calculate the cube so the cube of the string is not possible that's why we are doing type casting  
    for j in lis:       # loop on list 
        sum1+=j*j*j     # here we are calculating the cube of single digit and adding it in variable called sum1 it can also be written as  sum1=sum1+(j*j*j) 
    if a==sum1:         # if the original number from user and the number which we have calculated the cube of each digit and did sum will be same then it will print its a armstron number
        print("Its a armstrong number")
        a=input("Continue(Y/N)")
        if a=="N":
            break
        else:
            print("invalid input")
    else:
        print("Its not a armstrong number")
        a=input("Continue(Y/N)")
        if a=="N":
            break
        else:
            print("invalid input")
    
