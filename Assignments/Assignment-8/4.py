# question -4
def table(no_of_table,range_table):
    print("No of tables=",no_of_table,"\nRange Table=",range_table,"\n")
    for i in range(1,no_of_table+1):
        for j in range(1,range_table+1):
            print(i," x ",j,"=",i*j)
        print("\n")
    return 
table(10,10)
