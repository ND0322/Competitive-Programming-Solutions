n = int(input())

friends = {}
time = -1
for i in range(n):
  act,friend = map(str,input().split(" "))
  friend = int(friend)

  if act == "W":
    time = time + friend - 1
  else:
    time = time + 1

  if act != "W":

    if act == "R":
      if friend in friends:
        friends[friend][0] = time
      else:
        friends[friend] = [time,0]
    else:
      friends[friend][1] = friends[friend][1] + (time - friends[friend][0])
      friends[friend][0] = -1

friends = dict(sorted(friends.items()))

for i in friends:
  if friends[i][0] == -1:
    print(i,friends[i][1])
  else:
    print(i,-1)
