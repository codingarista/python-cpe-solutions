#11743 Credit Check

n = int(input())

for k in range(n):
  xs = input()  .split()
  sum = 0
  for s in xs:
    for i in range(len(s)):
      if i % 2 == 0:   #因為要index是偶數
        tmp = int(s[i]) * 2
        sum += tmp // 10  #負責拿十位數
        sum += tmp % 10   #負責拿個位數
      else:
        sum += int(s[i])
        
  if sum % 10 == 0:
    print("Valid")
  else:
    print("Invalid")
  