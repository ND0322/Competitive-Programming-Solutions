#todo

l = []

while (res := input()) != "0":
  l.append(res)

if len(l) == 1:
  print(l[0])

temp= ""
ans = ""
big = 0
for i in l:


  cur = "".join(i)

  if cur in temp:
    temp= temp[temp.index(cur) + 1:]
  temp= temp+ "".join(i)
  if len(temp) > big:
    big = len(temp)
    ans = temp

for i in ans:
  print(i)
