while True:
  n = int(input())

  if n == 0:
    break
  
  cnt = 0
  r = n * n
  for i in range(1,n+1):

    
    cnt += int((r-i*i) ** (1/2)) + 1
  cnt = cnt * 4
  cnt += 1
  

  print(cnt)
