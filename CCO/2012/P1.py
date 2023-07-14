def solve(n,o):


  
  if n == 0:
    if o == 0 or digits[0] or digits[1]:
      return True
    return False

  if o <= 0 or n < 0:
    return False  

  if (n,o) not in dp:
    for i in di:
      res = False
      if i != 0 and n % i == 0:
        res = solve(n // i,o-1)
      res = res or solve(n-i,o-1)
  
      if res:
        dp[(n,o)] = True
        return True
    dp[(n,o)] = False
  return dp[(n,o)]

w = int(input())
digits = [False] * (10)
di = set()
dp = {}

for i in range(int(input())):
  p = int(input())
  digits[p] = True
  di.add(p)

q = int(input())

for i in range(q):
  if solve(int(input()),w+1):
    print("Y")
  else:
    print("N")
