curLast = int(input())
curFirst = int(input())

count = 2

while curFirst <= curLast:

  next = curLast - curFirst

  curLast = curFirst
  curFirst = next

  

  count += 1

print(count)
