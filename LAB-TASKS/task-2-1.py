total_amount=0
while True:   # it will run the the program untill we select quit 
    user = input("press D for Deposit\npress W for Withdraw\npress Q for Quit ") # asking user to for Deposit,Withdraw or Quit
    if user=="D":                 
        amount=int(input("Enter the amount you want to deposit "))   
        total_amount=total_amount+amount       # formula for the deposit
    elif user=="W":
        amount=int(input("Enter the amount you want to withdraw "))
        if total_amount<amount:                # if the withdrawal amount will less than the total amount in the accont then it will print insufficent balance
            print("Insufficent balance ")
        else:
            total_amount=total_amount-amount
    elif user=="Q":                   # if user chooses Quit it will stops the while loop for  forever and will print the total amount
        break
    
    else:
        print("Wrong input try again") # if user not choosing "D" or "Q" or "W"  then it will display wrong input 

print("Total_amount",total_amount)
        


 
    
        
        
    
