#11461

import math

while True:
    n = input()
    if n == "0 0":
        break
    else:
        nn = n.split()
        r = int(nn[1]) ** 0.5



    print(math.floor(r))


# 1 4    1~2
# 1 10   1~3...
# 0 0

#output
#2
#3

#無條件進位 無條件捨去