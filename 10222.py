#10222

encode = "ertyuiop[]dfghjkl;'cvbnm,."
org =    "qwertyuiopasdfghjklzxcvbnm"

while True:
    try:
        n = input()
    except EOFEorror:
        break

    ret = ""
    for c in n:
        if c == ' ':
            ret += " "
        else:
            ret += org[encode.index(c.lower())]

    print(ret)
