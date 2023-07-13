n = int(input())

currentHigh = ""
highestBid = 0
for i in range(1, n+1):
  
  name = input()
  bid = int(input())

  if bid > highestBid:
    highestBid = bid
    currentHigh = name

print (currentHigh)
