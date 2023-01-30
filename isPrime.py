targetNum = 100
num = 3
while num <= targetNum:
    isPrime = False
    divid=2
    while divid < num:
        if num % divid == 0:
            isPrime = False
            break
        else:
            isPrime = True
        divid += 1
    if isPrime == True:
        print(num)
    num += 1
