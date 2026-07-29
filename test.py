#10922 - 2 the 9s

while True:
    s = input()
    if s == '0':
        break
    else:
        c = sum([int(x) for x in s])
        #print(c)

        if c % 9 != 0:
            print(s+ ' is not a multiple of 9.')
        else:
            count = 1

            while True:
                if c == 9:
                    break
                else:
                    cc = str(c)
                    c = sum([int(y) for y in cc])
                    count += 1

            print(s + ' is a multiple of 9 and has 9-degree '+ str(count) +'.')




#c = [int(x) for x in p]

#9 is a multiple of 9 and has 9-degree 1.

#is not a multiple of 9.


# Sample Input
# 999999999999999999999
# 9
# 9999999999999999999999999999998
# 0

# Sample Output
# 999999999999999999999 is a multiple of 9 and has 9-degree 3.
# 9 is a multiple of 9 and has 9-degree 1.
# 9999999999999999999999999999998 is not a multiple of 9.