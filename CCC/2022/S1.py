n = int(input())
numPossible = 0



  
for i in range(0,n):

  
  if (n - (i * 5)) % 4 == 0 and (n - (i * 5)) >= 0:
    numPossible += 1
  

print(numPossible)
