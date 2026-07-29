#10642

n = int(input())

lst = []
d = 0
count = 0
s = 0

for i in range(n):
    nn = input().split()
    #lst.append(nn)
    # int_lst = []
    # for elm in nn:
    #     int_lst.append(int(elm))

    # nn = [int(elm) for elm in nn]

    p1 = (int(nn[0]), int(nn[1]))
    p2 = (int(nn[2]), int(nn[3]))

    p1_s = sum(p1)
    p2_s = sum(p2)

    result = 0
    for j in range(p1_s, p2_s):
        result += j

    result += p2_s - p1_s

    result -= p1[0]

    result += p2[0]

    print("Case %d: %d" % (i+1, result))



#i+1 從0開始跑

# 3
# 0 0 0 1
# 0 0 1 0
# 0 0 0 2

#Case 1: 1