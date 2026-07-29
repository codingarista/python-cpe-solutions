#12019  Dooms Day Algorithm

n = int(input())

months = [31,28,31,30,31,30,31,31,30,31,30,31]

d = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

for i in range(n):
    w = 6   #每一輪要重置

    nn = input().split()

    date = int(nn[1])
    m = int(nn[0])
    days = sum(months[:m-1])
    days = days + (date - 1)
    w = (w + days) % 7   #days 經過天數
    print(d[w])



# Sample Input
# 8
# 1 6
# 2 28
# 4 5
# 5 26
# 8 1
# 11 1
# 12 25
# 12 31


# Sample Output
# Thursday
# Monday
# Tuesday
# Thursday
# Monday
# Tuesday
# Sunday
# Saturday