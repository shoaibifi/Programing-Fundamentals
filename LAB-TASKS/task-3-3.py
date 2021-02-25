a = int(input("Enter the ten digit integers "))   
b = str(a)     # here we are doing type casting because we are wanting to run a loop on input that we got from user 
lis = []
count=0
for i in b:    # running a loop on input
    lis.append(int(i))    # appending a input into a list also doing type casting, changing str into int because we have to compare the values we can compare the string nubers but we want to same number taht we got from user 
max1=lis[0]               # we are taking a digit from list that we will compare to find the maximum number
for j in lis:              # loop on lis
    if j>max1:             # comparing the max1 digit with members of lis on each iteration if the value of j will be greater than maximum number will be swapped 
        max1=j                 
for k in lis:              # here we are runnin loop on list to count the number of occurence of the maximum number 
    if max1==k:             # on each iteration if max1 value will be equal to the value of list then 1 will be added to the count
        count+=1
print("Maximum number", max1)
print("No of occurence of maximum number",count)
    

