t = int(input())
n = int(input())

ch = []

for i in range(n):
  ch.append(int(input()))

ch.sort()


for i in range(len(ch)):

  if ch[i] > t:
    print(i)
    break
  else:
    t-=ch[i]
