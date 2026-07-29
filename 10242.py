# 10242 Fourth Point!!


import math

while True:
    try:
        n = input()
    except EOFError:
        break

    nn = n.split()

    x1 = float(nn[0])
    y1 = float(nn[1])
    x2 = float(nn[2])
    y2 = float(nn[3])
    x3 = float(nn[6])
    y3 = float(nn[7])

    xx = x3 - x2 + x1
    yy = y3 - y2 + y1



    print('%.3f %.3f' %(xx,yy))



#xx = x3 - x2 + x1
#yy = y3 - y2 + y1


# 0.000 0.000 0.000 1.000 0.000 1.000 1.000 1.000
# 1.000 0.000 3.500 3.500 3.500 3.500 0.000 1.000
# 1.866 0.000 3.127 3.543 3.127 3.543 1.412 3.145

# 範例輸出 #1
# 1.000 0.000
# -2.500 -2.500
# 0.151 -0.398