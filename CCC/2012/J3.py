import sys

"""
sys.stdin = open("cowsignal.in","r")
sys.stdout = open("cowsignal.out","w")
"""


k = int(input())

m = 3
n = 3

ans = [[""] * (k*n) for i in range(k*m)]

icon = [["*","x","*"],[" ","x","x"],["*"," ","*"]]



for i in range(m):
  for j in range(n):
    for l in range(i*k,i*k+k):
      for y in range(j*k,j*k+k):
        ans[l][y] = icon[i][j]

for i in ans:
  print("".join(i))
