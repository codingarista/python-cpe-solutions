#10789

def isPrime(x):
  if x == 1:
    return False
    
  r = int(x**0.5)
  for i in range(2, r+1):
    if x % i == 0:
      return False

  return True

n = int(input())
count = 1
for i in range(n):
  s = input()

  d = {}
  for c in s:
    if c in d:
      d[c] += 1
    else:
      d[c] = 1

  print(d)
  sd = dict(sorted(d.items()))
  print(sd)
  
  print("Case", count)
  isPrint = False
  for k, v in sd.items():
    if isPrime(v):
      isPrint = True
      print(k, end="")
  if not isPrint:
    print("empty")
  else:
    print()

  count += 1
  