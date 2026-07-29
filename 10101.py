#10101

t = 1

while True:
    try:
        n = input()
    except EOFEorror:
        break

    div = [2, 1, 2, 2, 2, 1, 2, 2, 1]
    slot = []

    for idx in div:
        # if n == "":
        #     break

        num = n[-idx:]
        if num == '':
            num = 0
        else:
            num = int(num)
        # slot.append(n[-idx:])

        slot.append(num)
        n = n[:-idx]

       # t.append(n[-2:])

    slot = slot[::-1]
    print(slot)

    unit = ['kuti', 'lakh', 'hajar', 'shata']
    print(unit)

    isKuti = False  #判斷高位數有東西輸出
    count =  0
    print("%4d. " % t, end='')


    for i in range(4):
        if slot[i] != 0:
            print(slot[i], unit[i], end=' ')
            isKuti = True

        count += 1  #印到第幾位

    if slot[count] != 0:
        print(slot[count], end=' ')
        count += 1
        isKuti = True

    if isKuti:
        print("kuti", end=' ')

    for i in range(1, 4):
        if slot[count-1+i] != 0:
            print(slot[count-1+i], unit[i], end=' ')

    if slot[-1] != 0:
        print(slot[-1])

    t += 1