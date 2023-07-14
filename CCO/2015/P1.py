import sys

#todo



sAns = 0
bAns = 0

n,w = map(int,input().split(" "))

food = []

for i in range(n):
  food.append(int(input()))



def solve(i,last):
  if i == n:
    return 0

  if i > n:
    return float("inf")



  return min(solve(i+1,food[i]) + abs(food[i] - last),solve(i+1,w) + abs(food[i] - last))


"""
5 0
23
30
48
42
49
"""

food.sort()

last = w

for i in food:
  sAns += min(abs(i - last),abs(i-w))
  last = i

food = food[::-1]

ans = 0

last = w

for i in food:

  ans += min(abs(i - last),abs(i-w))
  last = i

sAns = min(sAns,ans)



food.sort()


a = food[:n//2]
b = food[n//2:]

b = b[::-1]

f = []

for i in range(n//2):
  f.append(a[i])
  f.append(b[i])

if n % 2 != 0:
  f.append(b[-1])

food = f

last = w

for i in food:
  bAns += max(abs(i - last),abs(i-w))

  last = i


food = food[::-1]

last = w

ans = 0

for i in food:
  ans += max(abs(i - last),abs(i-w))

  last = i

bAns = max(bAns,ans)

print(sAns,bAns)

"""
bAns = solve(0,w)

food.sort(reverse = True)

bAns = min(bAns,solve(0,w))
"""

"""

l = 0
r = n-1
last = w



while l <= r:
  
  temp = min(abs(last - food[l]), abs(last - food[r]),abs(w - food[r]),abs(w-food[l]))

  if temp == abs(last - food[l]) or temp == abs(w-food[l]):
    last = food[l]
    l+=1
    
  else:
    last = food[r]
    r-=1

  bAns += temp

l = 0
r = n-1
last = w



while l <= r:
  print(l,r)
  temp = max(abs(last - food[l]), abs(last - food[r]),abs(w - food[r]),abs(w-food[l]))

  if temp == abs(last - food[l]) or temp == abs(w-food[l]):
    last = food[l]
    l+=1
    
  else:
    last = food[r]
    r-=1

  sAns += temp



print(bAns,sAns)
"""
