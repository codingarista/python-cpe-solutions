#10415

d = {}

d['c'] = "0111001111"
d['d'] = "0111001110"
d['e'] = "0111001100"
d['f'] = "0111001000"
d['g'] = "0111000000"
d['a'] = "0110000000"
d['b'] = "0100000000"

d['C'] = "0010000000"
d['D'] = "1111001110"
d['E'] = "1111001100"
d['F'] = "1111001000"
d['G'] = "1111000000"
d['A'] = "1110000000"
d['B'] = "1100000000"


n = int(input())

for i in range(n):
    s = input()

    pre = "0000000000"
    stat = [0] * 10

    for c in s:
        for i in range(len(d[c])):
            if pre[i] != d[c][i] and pre[i] == '0':
                stat[i] += 1

        pre = d[c]

    # print(stat)
    print(*stat)   #*去括號



# 3
# cdefgab
# BAGFEDC
# CbCaDCbCbCCbCbabCCbCbabae


