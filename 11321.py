#11321

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

for e in lst:
    print(e)

# for q in range(len(lst)):
#     print(lst[q])


end = input()  #0 0

# 先利用每個數字除以M的餘數由小到大排，
#若排序中比較的兩數為一奇一偶且兩數除以M 的餘數相等，則奇數要排在偶數前面。
#若兩奇數除以M餘數大小相等，則原本數值較大的奇數排在前面。
#同樣的，若兩偶數除以M餘數大小相等，則較小的偶數排在前面。
#至於負數的餘數計算和 C 語言裡的定義相同，即負數的餘數絕對不會大於零。
#例如 -100 MOD 3 = -1, -100 MOD 4 = 0 依此類推。

#python 預設mod出來都會是正數   但c不會有這個問題, 算出來是正就是正，該負就會負

#sorted(     , key = lambda s: s[2])

# Sample Input
# 15 3
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 0 0