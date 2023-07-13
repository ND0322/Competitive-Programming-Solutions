import sys

sys.setrecursionlimit(10**6)
d = int(input())

clubs = []

for _ in range(int(input())):
  clubs.append(int(input()))

dp = {}


def solve(n):
  if n < 0:
    return 99999999
  if n == 0:
    return 0

  if n not in dp:
    res = float("inf")
    for i in clubs:
      if i <= n:
        ans = 1 + solve(n - i)

        if ans < res:
          res = ans
    dp[n] = res
  return dp[n]

ans = solve(d)

if ans != float("inf"):
  print("Roberta wins in",ans,"strokes.")
else:
  print("Roberta acknowledges defeat.")
