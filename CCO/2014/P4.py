n,p = map(int,input().split(" "))

planets = {}



for i in range(n):
  x,y = map(int,input().split(" "))
  if i+1 == p:
    ans1 = x

  if y <= x:
    planets[i+1] = (x,y)



planets = dict(sorted(planets.items(),key = lambda x:x[1][1]))




ans2 = 1

for key in planets:

  if key == p:
    continue

  if planets[key][1] <= ans1:
    ans1 += planets[key][0] - planets[key][1]
    ans2 += 1
  else:
    break


    






print(ans1)
print(ans2)
