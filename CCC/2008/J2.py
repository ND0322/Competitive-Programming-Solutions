p = "ABCDE"

while True:


  b = int(input())

  n = int(input())

  if b == 4 and n == 1:

    break

  if b == 1:
    
    p = p[n%5:] + p[:n%5] 
  if b == 2:

    p = p[-n%5:] + p[:-n%5] 
    


    

  if b == 3:
    if n % 2 == 0:
      continue
    else:
      temp = p[0]
      p = p[1] + p[1:]
      p = p[0] + temp + p[2:]

ans = ""

for i in p:
  ans += i + " "

print(ans.strip())
