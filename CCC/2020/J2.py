t = int(input())
num = int(input())
inf = int(input())

total = 0


if num > t:
  print(0)
else:
  
  for i in range(100000000):
    total += num * (pow(inf,i))
    if total > t:
      print(i)
      break
