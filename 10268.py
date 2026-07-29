#10268 - 498-bis

while True:
    try:
        x = int(input())
        p = input().split()
        # print(p)
        c = [int(x) for x in p]
        # print(c)


    except EOFError:
        break

    f = len(c)-1
    ans = 0

    for i in range(f):
        ans = ans + c[i]*(f-i)*(x**(f-(i+1)))


    print(ans)



# Sample Input
# 7
# 1 -1
# 2
# 1 1 1

# Sample Output
# 1
# 5