temps = {}

while True:
  p,t = map(str,input().split(" "))

  temps[p] = int(t)
  if p == "Waterloo":
    break


print(sorted(temps.items(),key = lambda x:x[1])[0][0])
