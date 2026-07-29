#490 Rotating Sentences

sen = []

max_len = 0

while True:
    try:
        s = input()
    except EOFError:
        break

    if max_len < len(s):
        max_len = len(s)

    sen.append(s)

for i in range(len(sen)):
    sen[i] += ' '*(max_len-len(sen[i]))

for i in range(max_len):
    for j in range(len(sen)-1, -1, -1):
        print(sen[j][i], end='')
    print()


# Sample Input
# Rene Decartes once said,
# "I think, therefore I am."
