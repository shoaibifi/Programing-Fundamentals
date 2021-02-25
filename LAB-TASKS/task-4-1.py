a = [1,3,5]
print("list 'a' ",a)
b = [2,4,6]
print("list 'b'",b)
c = []
for i in a:
    c.append(i)
for j in b:
    c.append(j)
print("The list 'c' after adding list 'a' and list 'b' is ",c)
max1=c[0]
for i in c:
    if i>max1:
        max1=i
print("The maximum value in the list 'c' is ",max1)
c.insert(4,42)
print("The list 'c' after inserting  fourth element",c)
c.extend([7,8,9])
print("The list 'c' after appending 7,8,9",c)
d = 0  # here we are wanting to print first and 2nd member of a list, for that we will take a variable and until the value of variable two it will print the members from list it when the value of variable becomes 2 it will break will stop the loop and we will got the first two members from the list  
for i in c:
    d+=1
    if d>=3:
        break
    else:
        print(i) # printing the first and the second member of the list
last = 0
for j in b:
    last=j
print("The last element of list 'b' without using its length is ",last)
counter=0
for k in a:
    counter+=1
print("The length of list 'a' without using its length is ",counter)
    
    


        



