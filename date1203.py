n = int(input())

u = 0

for i in range(n):
    s = input().split()  #可以直接一起
    s = s[1:]
    m = len(s)
    r = []
    for e in s :
        r.append(int(e))
    r.sort()

    if m % 2 != 0:
        u = m // 2
        w = r[u]
    else:
        u = m // 2
        v = u - 1
        w = (r[u] + r[v]) / 2
    sum = 0
    for j in r :
        count = abs(j - w)

        sum += count

    print(int(sum))






