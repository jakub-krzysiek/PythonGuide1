def silnia(n):
    #5! = 1*2*3*4*5
    res = 1
    for x in range(1,n+1):
        res = res * x
    return res

for number in lines:
    print(silnia(number))

#print(silnia(5))