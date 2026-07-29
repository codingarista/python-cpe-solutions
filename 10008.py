#10008

n = int(input())

d = {}

for i in range(n):
    nn = input()
    for c in nn:
        c = c.upper()
        if c in "QWERTYUIOPASDFGHJKLZXCVBNM":
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

# print(d)

lst = sorted(d.items(), key=lambda item: (item[1], -ord(item[0])), reverse=True)

# print(lst)

for t in lst:
    print(t[0], t[1])




#sorted(iterable, cmp=None, key=None, reverse=False)

#{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}