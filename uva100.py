#100 - The 3n + 1 problem

def cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 1:
            n = 3*n + 1
        else:
            n = n // 2
            
        count += 1
    
    return count

# print(cycle_length(22))

while True:
    try:
        n = input()
    except EOFError:
        break

    s = n.split()
    a = int(s[0])
    b = int(s[1])
    
    if a > b:
        x, y = b, a
    else:
        x, y = a, b
            
    max_len = 0
    for i in range(x, y+1):
        cl = cycle_length(i)
        if max_len < cl:
            max_len = cl
            
    print(a, b, max_len)
        
    