n = int(input())

for i in range(n):
    result = [0] * 10
    t = int(input())

    for j in range(1, t+1):
        s = str(j)
        for c in s:
            result[int(c)] += 1

    for r in result:
        print(r, end=' ')
    print()
