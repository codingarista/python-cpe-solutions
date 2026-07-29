#913 Joana and the Odd Numbers

while True:
    try:
        n = int(input())
    except EOFError:
        break

    r = (n+1)//2
    a = ((1 + n)*r)//2

    last = a*2-1
    print((last-2)*3)


