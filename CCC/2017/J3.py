start = input().split(" ")
end = input().split(" ")
t = int(input())




numMoved = 0

numMoved += abs(int(start[0]) - int(end[0]))
numMoved += abs(int(start[1]) - int(end[1]))

numExt = t - numMoved

if numExt < 0:
  print("N")
else:
  if numExt % 2 == 0:
    print("Y")
  else:
    print("N")
