n = int(input())
for i in range(n):
  ans = ""
  t = input()
  last = 0
  for j in range(1,len(t)):
    if t[j] != t[j - 1]:
      
      ans += str(j - last) + " " + str(t[j - 1]) + " "
      last = j


  ans += str(len(t[last:len(t)])) + " " + t[-1]
  print(ans)
