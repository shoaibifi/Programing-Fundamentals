def women():
    name = input("Hello Ma'am please enter your name ")
    bodyWeight = int(input("Enter your body weight "))
    wristAtfull = int(input("Enter your wrist measurement (at fullest point)"))
    wristAtnavel = int(input("Enter your wrist measurement (at navel point)"))
    hipAtfull = int(input("Enter your hip measurement (at fullest point)"))
    forstreamAtfull = int(input("Enter your forstream measurement (at fullest point)"))
    
    A1 = (bodyWeight*0.732) + 8.987
    A2 =  wristAtfull / 3.140
    A3 = wristAtnavel * 0.157
    A4 = hipAtfull*0.249
    A5 = forstreamAtfull * 0.434 
    B = A1+A2-A3-A4+A5
    BodyFat = bodyWeight-B
    BodyFatPerecentage  = (BodyFat*100)/bodyWeight 
    return print("       Hello",name,"\n\nYour Body fat: ",BodyFat,"\nYour Body Fat Percentage = ",BodyFatPerecentage)
    
    
def men():
    name = input("Hello sir please enter your name")
    bodyWeight = int(input("Enter the body weight "))
    wristMeasurment = int(input("Enter the Wrist measurment "))
    A1 = (bodyWeight*1.082) + 94.42
    A2 = wristMeasurment * 4.15
    B = A1-A2
    bodyFat = bodyWeight-B
    bodyFatPercentage = (bodyFat * 100)/bodyWeight
    return print("      Hello",name,"\n\nYour Body fat: ",bodyFat,"\nYour Body Fat pecentage is",bodyFatPercentage)

def cal():
    a = input("Press '1' to calculate body weight of men\nPress '2' to calculate body weight of women ")
    if a=="1":
        b = men()
        return b
    elif a=="2":
        b = women()
        return b
    else :
        print("Wrong input")
cal()
