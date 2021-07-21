# qno-3 with while loop
def checkArm(o):
    num = o
    b = 0
    arm = 0
    while num>0:
        s = num%10
        arm += s*s*s
        num =  num//10
    if o == arm:
        return True
    else:
        return False
    
