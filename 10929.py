while True:
    n = input()
    if n == '0':
        break
    else:
        osum = 0
        esum = 0
        for i in range(len(n)):
            if i % 2 != 0:
                osum = int(n[i]) + osum
            else:
                esum = int(n[i]) + esum

    if (osum - esum) % 11 == 0 :
        print(n,"is a multiple of 11.")
    else:
        print(n,"is not a multiple of 11.")


# is not a multiple of 11.
