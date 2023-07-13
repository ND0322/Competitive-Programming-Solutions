a = input()
notBroke = True
liste = ['I','O','S','H','Z','X','N']

for i in a:
  if i not in liste:
    print("NO")
    notBroke = False
    break
if notBroke:
  print("YES")
