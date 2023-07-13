n = int(input())

l1 = ["A","B","C"]
l2 = ["D","E","F"]
l3 = ["G","H","I"]
l4 = ["J","K","L"]
l5 = ["M","N","O"]
l6 = ["P","Q","R","S"]
l7 = ["T","U","V"]
l8 = ["W","X","Y","Z"]


for _ in range(n):
  

  

  
  s = ""

  
  for i in input():
    if i.isalnum():
      s += i
    if len(s) == 10:
      break
      
    
  
  
  
  

  ans = ""
  for i in range(10):
    if s[i] in l1:
      ans += "2"

    if s[i] in l2:
      ans += "3"
    elif s[i] in l3:
      ans += "4"
    elif s[i] in l4:
      ans += "5"
    elif s[i] in l5:
      ans += "6"
    elif s[i] in l6:
      ans += "7"
    elif s[i] in l7:
      ans += "8"
    elif s[i] in l8:
      ans += "9"
    elif s[i].isnumeric():
      ans += s[i]

    

  ans = ans[0:3] + "-" + ans[3:6] + "-" + ans[6:]
  print(ans)
