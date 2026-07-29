#10420

n = int(input())   #n  資料筆數習慣用n

d = {}

for i in range(n):
    s = input().split()
    ss = s[0]

    if ss in d:
        d[ss] += 1
    else:
        d[ss] = 1

for key, value in d.items():
    print(key,value)

countryDict = dict(sorted(d.items()))

for k, v in countryDict.items():
    print(k, v)



# Sample Input
# 3
# Spain Donna Elvira
# England Jane Doe
# Spain Donna Anna
#
#
# Sample Output
# England 1
# Spain 2