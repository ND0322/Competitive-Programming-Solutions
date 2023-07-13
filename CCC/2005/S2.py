m,n = map(int,input().split(" "))

x = 0
y = 0

while True:
  tx,ty = map(int,input().split(" "))

  if tx == 0 and ty == 0:
    break

  if x + tx <= 0:
    x = 0
  elif x + tx >= m:
    x = m
  else:
    x += tx
  
  if y + ty <= 0:
    y = 0
  elif y + ty >= n:
    y = n
  else:
    y += ty
  print(x,y)
