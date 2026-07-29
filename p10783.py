#10783

n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())

    if a % 2 == 0:
        a += 1
    if b % 2 == 0:
        b -= 1

    print(sum(list(range(a, b+1, 2))))



#2 10

#3 9

