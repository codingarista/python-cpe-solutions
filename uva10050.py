#10050

n = int(input())



for i in range(n):

    d = int(input())

    result = [0] * (d+1)



    p = int(input())



    h = []

    for j in range(p):

        h.append(int(input()))



    for hh in h:

        for s in range(0, d+1, hh):

            result[s] += 1



    count = 0;

    for x in range(1, d+1):

        day = (x-1) % 7

        if result[x] != 0:

            if not(day==5 or day==6):

                count += 1



    print(result)

    print(count)

