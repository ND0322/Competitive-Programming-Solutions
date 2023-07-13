target = {}
s = {}

mismatch = 0

for i in sorted(input()):
  if i in target:
    target[i] += 1
  else:
    target[i] = 1
    
for i in sorted(input()):
  if i in s:
    s[i] += 1
  else:
    s[i] = 1



for i in target:
  totalOf = target[i]
  sub = 0
  if i in s:
    sub = s[i]

  mismatch += abs(totalOf - sub)


if "*" in s:
  
 mismatch -= s["*"]


if mismatch <= 0:
  print("A")
else:
  print("N")
