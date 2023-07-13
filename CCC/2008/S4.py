def solve(i,stack):




  if i == 3 and len(stack) == 1:


    return stack[0]

  ans = 0
  if i < 3:
    
    nxt = stack.copy()
    nxt.append(cards[i+1])
  
    res = solve(i+1,nxt)
    if res <= 24:
      ans = max(res,ans)

  if len(stack) > 1:
    nxt = stack.copy()

    a = nxt.pop()
    b = nxt.pop()

    nn = nxt.copy()

    nn.append(a+b)


    
    res = solve(i,nn)

    if res <= 24:
      ans = max(res,ans)

    nn = nxt.copy()

    nn.append(a-b)

    res = solve(i,nn)
    if res <= 24:
      ans = max(res,ans)

    nn = nxt.copy()

    nn.append(b-a)

    res = solve(i,nn)
    if res <= 24:
      ans = max(res,ans)



    nn = nxt.copy()

    nn.append(a*b)

    res = solve(i,nn)
    if res <= 24:
      ans = max(res,ans)

    nn = nxt.copy()

    if b != 0 and a % b == 0:
      nn = nxt.copy()

      nn.append(a//b)
  
      res = solve(i,nn)
      if res <= 24:
        ans = max(res,ans)

    if a != 0 and b % a == 0:
      nn = nxt.copy()

      nn.append(b//a)
  
      res = solve(i,nn)
      if res <= 24:
        ans = max(res,ans)
        
  return ans
      

    

    

    
  

n = int(input())

for i in range(n):
  cards = []
  cards.append(int(input()))
  cards.append(int(input()))
  cards.append(int(input()))
  cards.append(int(input()))

  cards.sort()
  print(solve(0,[cards[0]]))
