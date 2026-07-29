while True:
    n = input().split()
    if n[0]=='0' and n[1]=='0':
        break
    else:
        if len(n[1]) > len(n[0]):
            n[0] = "0" * (len(n[1])-len(n[0])) + n[0]
        else:
            n[1] = "0" * (len(n[0])-len(n[1])) + n[1]
        # print(n)

    carry_count = 0
    carry = False
    for i in range(len(n[0])-1, -1, -1):
        if carry == False:
            add = 0
        else:
            add = 1

        if int(n[0][i]) + int(n[1][i]) + add >= 10:
            carry_count += 1;
            carry = True
        else:
            carry = False

    if carry_count == 0:
        print("No carry operation.")
    else:
        print(carry_count, "carry operation.")
