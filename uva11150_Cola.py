#11150
#最多總共只會借一個瓶子

while True:
    try:
        n = int(input())
    except EOFError:
        break

    emp = 1
    full= n
    count = n

    while True:
        sum = full+emp

        full = sum // 3
        emp = sum % 3

        count += full

        if full+emp < 3:
            break

    print(count)