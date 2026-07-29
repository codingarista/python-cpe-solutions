#10038 - Jolly Jumpers

while True:
    try:
        n = input().split()
    except EOFError:
        break

    n = n[1:]

    arr = []
    Jolly = True

    for i in range(1,len(n)):
        s = abs(int(n[i])-int(n[i-1]))
        arr.append(s)

    a = sorted(arr)

    if a == list(range(1, len(n))):
        print("Jolly")
    else:
        print("Not Jolly")


#Jolly
#Not Jolly

#4 1 4 2 3
#5 1 4 2 -1 6



# 4 1 4 2 3
# [1, 2, 3]
# Not Jolly
#  x = [1, 2, 3]
#  y = [1, 2, 3]
#  z = [1, 2, 2, 3]
#  x1 = [1, 2, 3, 4]
#  x == y
# True
#  x == z
# False
#  x ==x1
# False
#  a = range(10)
#  a
# range(0, 10)
#  b = list(range(10))
#  b
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 
# KeyboardInterrupt
# 
# KeyboardInterrupt
#  list(range(10,21))
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# 