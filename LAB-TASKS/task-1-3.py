def calculate_volume_and_circumference(radius,height):
    from math import pi
    r=radius
    h=height
    circumference=2*pi*r
    volume=pi*(r*r)*h
    return print("circumference=",circumference,"\nVolume",volume)
    
