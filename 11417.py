#11417

def GCD(i,j):
    while i !=0:
        i, j = j%i, i

    return j

# print(GCD(20, 52))

while True:
    n = int(input())
    G = 0
    if n == 0:
        break
    else:
        for i in range(1,n) :
            for j in range(i+1,n+1) :
                G += GCD(i,j)

    print(G)



