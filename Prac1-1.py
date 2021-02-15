import math
def One():
    x = int(input("x - "))
    y = int(input("y - "))
    z = int(input("z - "))
    m = math.sqrt((21*math.pow(y, 4) - y)/(math.pow(z, 2) + math.pow(z, 5) + 91)) + ((8*math.pow(y, 8) + math.pow(x, 6)+29) /
    (math.cos(y) - 85*math.pow(z, 3) + 54)) + (76*math.pow(x, 5) + 62*math.pow(y, 2))/((math.pow(y, 6)/49) + math.exp(y))
    print(m)

def Two():
    x = int(input("x - "))
    if x < 19:
        m = (math.pow(x, 2)/8) + 16*math.pow(x, 4)
        print(m)
    elif 19 <= x < 92:
        m = math.sin(math.fabs(x) - 28*math.pow(x, 6)) - math.pow(x, 5)
        print(m)
    elif 92 <= x < 112:
        m = 3*(math.exp(x) - math.fabs(x)) + math.pow(x, 6)
        print(m)
    elif 112 <= x < 148:
        m = math.pow(x, 8) - 8*math.pow(x, 3)
        print(m)
    else:
        m = math.pow((math.cos(x) - 87*math.pow(x, 5) - 59), 2) - 28*math.pow(x, 5)
        print(m)

def Three():
    n = int(input("n - "))
    m = int(input("m - "))
    k = 0
    f = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            k += (math.pow(j, 2) + math.pow(i, 8))
    for i in range(1, n+1):
        for j in range(1, m+1):
            f += (math.sin(i) - (math.pow(i, 2)/47))
            w = k - 79*f
    print(w)

def Four(n):
    if n == 0:
        return 10
    else:
        return math.cos(Four(n - 1)) - math.sin(Four(n - 1)) + 94

while True:
    choose = int(input("Выбор номера задания 1,2,3,4 (Любая другая цифра - Выйти) - "))
    if choose == 1:
        One()
    elif choose == 2:
        Two()
    elif choose == 3:
        Three()
    elif choose == 4:
        print(Four(int(input("n - "))))
    else:
        print("Завершение работы")
        break