#10193

n = int(input())

lst = []

def gcd(x,y):
    while x!= 0:
        x, y = y%x, x
    return y

#print(gcd(3,6))

for i in range(n):
    s1 = input()
    s2 = input()
    ss1 = int(s1,2)
    ss2 = int(s2,2)
#     print(ss1)
#     print(ss2)
    if gcd(ss1,ss2) != 1:
        print(f"Pair #{i+1}: All you need is love!")
    else:
        print(f"Pair #{i+1}: Love is not all you need!")


# class int(x, base=10)
