#uva10018

n = int(input())

for i in range(n):
    count = 0
    p = int(input())

    while True:
        q = int(str(p)[::-1])
        if p == q:
            print(count, p)
            break
        else:
            p += q
            count += 1









# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# https://www.w3schools.com/python/python_try_except.asp