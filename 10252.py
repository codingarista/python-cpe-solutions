#10252 Common Permutation

#統計 => 找共同次數的最小值 (最大公因數概念)
#s.count()  min(x,y)

alpha = 'abcdefghijklmnopqrstuvwxyz'

while True:
    try:
        s1 = input()
        s2 = input()
    except EOFError:
        break

    result = ''

    for c in alpha:
        count1 = s1.count(c)
        count2 = s2.count(c)
        min_value = min(count1, count2)

        result += c * min_value

    print(result)


# s = 'abcdddbccccddddd'
# >>> s.count('d')
# 8

#python 10252.py <t10252.txt

# Sample Input
# pretty
# women
# walking
# down
# the
# street
# Sample Output
# e
# nw
# et

