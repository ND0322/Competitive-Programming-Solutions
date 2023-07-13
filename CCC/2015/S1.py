n = int(input())
stack = []
for i in range(n):

  k = int(input())

  if k == 0:
    a = stack.pop(-1)
  else:
    stack.append(k)

print(sum(stack))
