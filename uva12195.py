#12195

t = {'W': 64, 'H': 32, 'Q':16, 'E': 8, 'S': 4, 'T': 2, 'X': 1}

while True:
    n = input()

    if n == '*':
        break
    else:
        s = n.split('/')

    count = 0
    for r in s:
        m = 0
        if r == '':
            continue
        else:
            for q in r:
                m += t[q]

            if m == 64:
                count += 1

    print(count)


#c,c++ array
#tab

