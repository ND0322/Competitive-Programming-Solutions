n = int(input())
tC = 0
sC = 0

for i in range(n):
  a = input().lower()
 
  for j in a:
    if j == "t":
      tC += 1
    elif j == "s":
      sC += 1
if tC > sC:
  print("English")
else:
  print("French")
