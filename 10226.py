#10226

n = int(input())
input()

A = {}
count = 0
while (True):
    s = input()

    if s == '':
        sortDict = dict(sorted(A.items()))
        for key, value in A.items():
            print(key, value/count)

        A = {}
        count = 0
    else:
        count+=1
        if s in A:
            A[s] += 1
        else:
            A[s] = 1

