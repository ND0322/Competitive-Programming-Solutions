def check(m,x,y):


  
  if x < 5**(m-1) or x > 3 * 5**(m-1):
    return "empty"

  
  if(x // 5**(m-1) == 2 and y < 2*5**(m-1)):
    
    return "crystal"

  
  if (x // 5**(m-1) != 2 and y >= 2*5**(m-1)):
    return "empty"

  
  if (x // 5**(m-1) == 1 or x // 5**(m-1) == 3) and y < 5**(m-1):
    return "crystal"
    
  
  if m == 1:
    return "empty"
  
  if y >= 2*5**(m-1):
    return check(m-1,x% (5**(m-1)),y%(2*5**(m-1)))
  
  return check(m-1,x% (5**(m-1)),y%(5**(m-1)))

t = int(input())

for _ in range(t):
  m,x,y = map(int,input().split(" "))
  print(check(m,x,y))
