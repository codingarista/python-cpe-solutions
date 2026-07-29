#13185

n = int(input())

for i in range(n):

    a = int(input())

    s = int(a ** 0.5)   #轉折點
    sum = 0
    for j in range(2,s+1):   #error
        if a % j == 0:
            sum += j
            if a // j != j:
                sum += a // j

    sum += 1

    if a > sum:
        print("deficient")
    elif a == sum:
        print("perfect")
    else :
        print("abundant")







