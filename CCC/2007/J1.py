day = 732555 + 87

n = int(input())

for i in range(n):
  y,m,d = map(int,input().split(" "))

  
  e = y * 365 + m * 30 + d

  if (day - e) // 365 >= 18:
    print("Yes")
  else:
    print("No")
