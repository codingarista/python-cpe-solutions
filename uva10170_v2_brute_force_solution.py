#10170  
v2 暴力解法

import math

n = input().split()

s = int(n[0])
d = int(n[1])

i = s
sum = 0
while sum < d:

    sum += i
    i += 1

print(i-1)

# c = -s*s + s - 2*d
# x = (-1 + ((1 - 4*c) ** 0.5)) / 2
#
# print(int(math.ceil(x)))