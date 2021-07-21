#qno-3 with for loop
def check_arm(x):
    b = str(x)
    l = len(b)
    arm = 0
    for i in range(l):
        arm += int(b[i])*int(b[i])*int(b[i])
    if x==arm:
        return True
    else:
        return False


