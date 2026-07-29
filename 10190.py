#10190 Divide, But Not Quite Conquer!

while True:
    try:
        s = input().split()
        n = int(s[0])
        m = int(s[1])

    except EOFError:
        break

    if n <= 1 or m <= 1:
        print('Boring!')
        continue   #回到while true

    a = []
    while True:
        if n % m == 0:
            a.append(n)
            n = n // m
        else:
            print('Boring!')
            break

        if n == 1:
            a.append(1)
            print(*a)
            # for e in a:
            #     print(e)
            break


# Sample Input
# 125 5
# 30 3
# 80 2
# 81 3
# Sample Output
# 125 25 5 1
# Boring!
# Boring!
# 81 27 9 3 1