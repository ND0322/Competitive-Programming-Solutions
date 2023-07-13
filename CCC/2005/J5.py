def isA(s):


  if len(s) == 1:
    if s == 'A':
      return True
    return False


  if len(s) == 2:
    return False

  

  if s[0] == 'B' and s[-1] == 'S' and isMonkey(s[1:len(s)-1]):
    return True
  return False

def isMonkey(s):


  if isA(s):
    return True


  for i in range(1,len(s)-1):
    if isA(s[:i]) and s[i] == 'N' and isMonkey(s[i+1:]):
      
      return True

  return False


while True:
  s = input()

  if s == 'X':
    break

  if isMonkey(s):
    print("YES")
  else:
    print("NO")
