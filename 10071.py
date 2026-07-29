#10071

while True:
    try:
        s = input().split()
        v = int(s[0])
        t = int(s[1])
        x = 2 * v * t
        print(x)
    except EOFError:
        break



# Sample Input
# 0 0
# 5 12
#
# Sample Output
# 0
# 120