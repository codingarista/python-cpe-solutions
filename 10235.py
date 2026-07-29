import math

while True:
    try:
        n = int(input())
    except EOFError:
        break

    isPrime = True
    s = int(n ** 0.5)
    for i in range(2,s+1):
        if n  %  i == 0:
            isPrime = False
            break

    isEmirp = True
    q = int(str(n)[::-1])
    print(q)
    ss = int(q ** 0.5)
    for i in range(2,ss+1):
        if q  %  i == 0:
            isEmirp = False
            break

    if isPrime:
        if isEmirp:
            print(n," is prime.")
        else:
           print(n," is not prime.")
    else:
        print(n," is Emirp.")







