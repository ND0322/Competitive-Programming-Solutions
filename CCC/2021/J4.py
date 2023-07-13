a = input()

lCount = 0
mCount = 0
sCount = 0

missL = 0
missM = 0
mInL = 0
lInM = 0

for i in a:
  if i == "L":
    lCount += 1
  elif i == "M":
    mCount += 1
  else:
    sCount += 1
desired = ""

desired += "L" * lCount
desired += "M" * mCount
desired += "S" * sCount

for i in range(len(a)):
  if a[i] == "M" and desired[i] != "M":
    missM += 1
  if a[i] == "L" and desired[i] != "L":
    missL += 1
  if a[i] == "L" and desired[i] == "M":
    lInM += 1
  elif a[i] == "M" and desired[i] == "L":
    mInL += 1
answer = missL + missM - min(mInL, lInM)

print(answer)
