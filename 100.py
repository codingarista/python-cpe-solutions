def cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 1:
            n = 3*n + 1
        else:
            n = n // 2

        count += 1

    return count

# print(cycle_length(22))

#1.輸入n
#2.印出n
#3.當n等於1時停止
#4.如果n是奇數，則N←3N+1
#5.其餘的狀況，則N←N/2
#6.回到第二步驟
#給予一個輸入22，則會印出下列的數列： 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1


while True:
    try:
        n = input()
    except EOFError:
        break

    s = n.split()
    a = int(s[0])
    b = int(s[1])

    if a > b:
        x, y = b, a
    else:
        x, y = a, b

    max_len = 0
    for i in range(x, y+1):
        cl = cycle_length(i)
        if max_len < cl:
            max_len = cl

    print(a, b, max_len)

