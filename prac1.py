import math
def One():
    x = int(input("x - "))
    y = int(input("y - "))
    z = int(input("z - "))
    m = math.sqrt((21*math.pow(y, 4) - y)/(math.pow(z, 2) + math.pow(z, 5) + 91) +
    ((8*math.pow(y, 8) + math.pow(x, 6) + 29)/(math.cos(y) - 85*math.pow(z, 3) + 54))
    +(76*math.pow(x, 5) + 62*math.pow(y, 2))/((math.pow(y, 6)/49) + math.exp(y)))
    print(m)
One()
