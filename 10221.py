# 10221 - Satellites

import math

while True:
    try:
        n = input()
    except EOFError:
        break

    n = n.split()
    s = int(n[0])
    a = int(n[1])
    r = 6440
    arc = 0
    sr = r + s

    if n[2] == "min":
        a = a/60
    arc = 2 * (r + s) * math.pi * (a / 360)

    c = (sr*sr + sr*sr - 2*sr*sr*math.cos(a*(math.pi)/180)) ** 0.5

    # print(arc,c)

    print('%.6f %.6f' % (arc, c))


# ('%.6f %.6f' % (arc, c)) c 會顯示四捨五入後的結果

# Here s is the distance of the satellite from the surface of the earth and a is the angle that the satellites make with the center of earth. It may be in minutes (′) or in degrees (◦).

#弧長

# 角度分秒 1°（度）= 60′

# 餘弦定理 c^2 = a^2 + b^2- 2ab*cosgamma


#
# Sample Input
# 500 30 deg
# 700 60 min
# 200 45 deg

# Sample Output
# 3633.775503 3592.408346
# 124.616509 124.614927
# 5215.043805 5082.035982