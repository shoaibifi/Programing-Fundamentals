### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget,bashir_budget):
    if ali_budget>bashir_budget:
        price = bashir_budget
    else:
        price = ali_budget
    for i in range(1,price+1):
        if ali_budget%i==0 and bashir_budget%i==0:
            a=i
    return a
           
#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###

def calculateProfit(ali_budget,bashir_budget):
    if type(ali_budget)==float or type(bashir_budget)==float:
        ali_budget=int(ali_budget)
        bashir_budget=int(bashir_budget)
    else:
        return "Not Possible"
    price = chocolatePrice(ali_budget,bashir_budget)
    if ali_budget>bashir_budget:
        ali_unit_price = price*3/2 
        bashir_unit_price = price*2

        
    if ali_budget<bashir_budget:
        ali_unit_price = price*2
        bashir_unit_price = price*3/2
        
    total_piece_ali =ali_budget/price
    total_piece_bashir =bashir_budget/price
    
    
    
    
    #--------------------------------Remove----------
    print("total_piece_ali :",total_piece_ali)
    print("total_piece_bashir :",total_piece_bashir)
    #--------------------------------Remove end----------
    
    ali_profit = (ali_unit_price *total_piece_ali) - ali_budget
    bashir_profit = (bashir_unit_price *total_piece_bashir) - bashir_budget
    
    #----------------------------------------------------------
    print("ali_profit :",ali_profit)
    print("bashir_profit :",bashir_profit)
    #----------------------------------    

    if ali_profit>bashir_profit:
        return ali_profit
    else :
        return bashir_profit
    
calculateProfit(12.2,8)
    

#### End OF MARKER


