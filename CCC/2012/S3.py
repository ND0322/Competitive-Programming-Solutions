n = int(input())

readings = {}


first = []
second = []
for i in range(n):
  r = int(input())

  if r not in readings:
    readings[r] = 1
  else:
    readings[r] += 1


readings = sorted(readings.items(), key = lambda x:x[1], reverse = True)

start = -1

target = readings[0][1]

for i in range(len(readings)):
  if readings[i][1] < target:
    start = i
    break
  first.append(readings[i][0])

target = readings[i][1]
for i in range(start,len(readings)):
  if readings[i][1] < target:
    break
  second.append(readings[i][0])


fmin = min(first)
fmax = max(first)
smin = min(second)
smax = max(second)


if len(first) > 1:

  print(abs(fmax - fmin))

else:
  print(max(abs(fmax - smin), abs(smax - fmin)))
