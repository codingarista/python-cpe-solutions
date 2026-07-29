#11192

while True:
    #直接讀數字
    #把輸入讀進來 (永遠優先)
    k = input().split()
    n = int(k[0])
    if n == 0:
        break
    else:
        s = k[1] #py3預設讀進來是字串

    c = len(s) // n    #長度
    result = ""
    for i in range(0, len(s), c):
        ss = s[i:(i+c)]
        # print(ss)
        result += ss[::-1]

    print(result)


# [::-1]
