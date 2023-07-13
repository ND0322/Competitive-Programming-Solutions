def s(n,k):
  if k <= 0:
    return n
  return n*10**k + s(n,k-1)

n = int(input())
k = int(input())

print(s(n,k))
