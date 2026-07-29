#11349

n = int(input())

for i in range(n):
    
    a = int(input().split()[2])
    
    # N = input().split()
    # a = int(N[2])
   
    arr = []
            
    for e in range(a):
       aa = input().split()
       arr.extend(aa)

    print(arr)
    
    print(arr[::-1])


    size = len(arr)
    isError = False
    for j in range(size//2):
        if arr[j] != arr[size-1-j]:
            isError = True
            break
    
    if isError:
        print("Test #%d: Non-symmetric." % (i+1))
    else:
        # print("Test #%d: Symmetric." % (i+1))
        print(f"Test #{i+1}: Symmetric.")

        
    
    
    if arr != arr[::-1]:
        print("Test #%d: Non-symmetric." % (i+1))
    else:
        # print("Test #%d: Symmetric." % (i+1))
        print(f"Test #{i+1}: Symmetric.")
