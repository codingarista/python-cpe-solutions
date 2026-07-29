#10931

while True:
  I = int(input())

  if I == 0:
    break

  lst = []
  count = 0
  while I != 0:
    if I%2 == 1:
      count += 1
    lst.append(I % 2)
    I = I // 2

  r = lst[::-1]
  print("The parity of ", end="")
  for e in r:
    print(e, end="")
  print(" is", count, "(mod 2).")