#10189

n = input().split()

nn = int(n[0])
m = int(n[1])

lst = []
new = []

for i in range(nn):
    b = input()
    lst.append(b)

    new.append([0] * m)

for j in range(nn):
    for k in range(m):
        if lst[j][k] == "*":
            if j-1 >= 0:
                if k-1 >= 0:
                    new[j-1][k-1] += 1

                new[j-1][k] += 1

                if k+1 < m:
                    new[j-1][k+1] += 1
            ######################
            if k-1 >= 0:
                new[j][k-1] += 1

            # new[j][k] += 1

            if k+1 < m:
                new[j][k+1] += 1

            ######################
            if j+1 < nn:
                if k-1 >= 0:
                    new[j+1][k-1] += 1

                new[j+1][k] += 1

                if k+1 < m:
                    new[j+1][k+1] += 1

for j in range(nn):
    for k in range(m):
        if lst[j][k] == "*":
            new[j][k] = "*"


for i in range(nn):
    print(*new[i])



# Sample Input
# 4 4
# *...
# ....
# .*..
# ....
# 3 5
# **...
# .....
# .*...
# 0 0
#
# Sample Output
# Field #1:
# *100
# 2210
# 1*10
# 1110
# Field #2:
# **100
# 33200
# 1*100