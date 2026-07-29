#10812 Beat the Spread!

n = int(input())


a = 0
b = 0

for i in range(n):
    t = input().split()

    a = (int(t[0]) + int(t[1])) // 2
    b = int(t[0]) - a

    if a < b or a < 0 or b < 0:
        print("impossible")
    else:
        print(a,b)


# Sample Input
# 2
# 40 20
# 20 40