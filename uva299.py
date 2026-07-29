#299 Train Swapping

n = int(input()) #int

for q in range(n):
    input()
    m = input().split()  #string
    count = 0
    for i in range(len(m)) :
        for j in range(len(m)-1):
            if int(m[j]) > int(m[j+1]):
                m[j], m[j+1] = m[j+1], m[j]
                count += 1

    print("Optimal train swapping takes", count, "swaps.")



#tmp = m[i+1]

#3
#3
#1 3 2
#4
#4 3 2 1
#2
#2 1


#Optimal train swapping takes 1 swaps.
#Optimal train swapping takes 6 swaps.
#Optimal train swapping takes 1 swaps.

