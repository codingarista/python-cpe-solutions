#10055

while True:
    try:
        n = input()
    except EOFError:
        break

    #不要打亂標準格式

    s = n.split()

    t = []

    for e in s :
        t.append(int(e))

    #全部都轉完才繼續做事 所以要跳出迴圈

    print(abs(t[1] - t[0]))