snakes = {54:19,90:48,99:77}
ladders = {9:34,40:64,67:86}



cur = 1

while True:
  move = int(input())

  if move == 0:
    print("You Quit!")
    break

  
  cur += move

  if cur > 100:
    cur -= move

  if cur in snakes:  
    cur = snakes[cur]
  if cur in ladders:
    cur = ladders[cur]
  
  print("You are now on square " + str(cur))

  if cur == 100:
    print("You Win!")
    break
