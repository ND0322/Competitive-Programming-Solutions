t = input()
s = input()
e = True
target = {s}

for i in range(len(s)):
  target.add(s[i:len(s)] + s[0:i]) 

for i in range(len(t) - len(s) + 1):
  if t[i:i+len(s)] in target:
    e = False
    print("yes")
    break
if e:
  print("no")
