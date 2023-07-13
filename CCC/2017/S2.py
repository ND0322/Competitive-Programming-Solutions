n = int(input())

ting = list(map(int,input().split()))

ting.sort()

low = ting[0:int(round(float(n)/2 + .1,0))]
high = ting[int(round(float(n)/2 +.1 ,0)) :n + 1]

low.sort(reverse = True)



ans = ""

for i in range(int(round(float(n)/2 + .1))):
  ans += str(low[i])
  ans += " "

  if i + 1 <= len(high):
    ans += str(high[i])
  ans += " "
print(ans)
