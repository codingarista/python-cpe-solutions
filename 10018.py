n = int(input())

for i in range(n):
    count = 0
    p = int(input())

    while True:
        q = int(str(p)[::-1])
        if p == q:
            print(count, p)
            break
        else:
            p += q
            count += 1
