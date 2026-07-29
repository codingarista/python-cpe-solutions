#11321  Sort! Sort!! and Sort!!!

n = input().split()

#15 3  n[0]

nn = int(n[0])

m = int(n[1])

lst = []

for i in range(nn):
    d = int(input())  #讀資料進來
    lst.append(d)   #先將資料蒐集好

def cmp_int(x,y):
    sx = 1
    sy = 1
    if x < 0:
        sx = -1
    if y < 0:
        sy = -1

    rx = (abs(x) % m) * sx
    ry = (abs(y) % m) * sy

    if rx == ry:
        if x % 2 != 0 and y % 2 == 0:
            return False
        elif x % 2 != 0 and y % 2 != 0:
            return x < y
        elif x % 2 == 0 and y % 2 == 0:
            return x > y
        else:
            return True
    elif rx > ry:
        return True
    else:
        return False

def bubbleSort(arr):
    for j in range(len(arr)):
        for k in range(len(arr)-1-j): #從末端減
            # if arr[k] > arr[k+1]:
            if cmp_int(arr[k], arr[k+1]):
                arr[k], arr[k+1] = arr[k+1], arr[k]
                #python tuple互換寫法(內容不可改但可以互換)

    return arr


lst = bubbleSort(lst)

for q in range(len(lst)):
    print(lst[q])


end = input()  #0 0


