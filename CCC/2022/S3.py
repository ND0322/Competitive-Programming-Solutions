n,m,k = map(int,input().split(" "))

ans = []

for i in range(n):
  s = n-i-1
  cur = min(k-s,m)

  if cur <= 0:
    break

  if cur > i:
    val = min(m,i+1)
    cur = val

  else:
    val = ans[i-cur]
  ans.append(val)
  k -= cur

ans = list(map(str,ans))
if len(ans) == n and k == 0:
  print(" ".join(ans))
else:
  print(-1)
    
