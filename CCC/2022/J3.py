n = input()

indexList = []
newList = []
lastSign = 0
signLocations = []

for i in range(0,len(n) - 1):
  if n[i].isdigit():
    if n[i + 1].isalpha():
      
      indexList.append(i)
  elif n[i] == "+" or n[i] == "-" :
    signLocations.append(i)
    
indexList.append(len(n) - 1)



for i in indexList:
 newList.append(n[lastSign:i + 1])
 lastSign = i+1


for i in range(len(newList)):
  letters = ""
  command = ""
  amount = ""

  
 
  
  for j in newList[i]:
    
    
    if j == "+":
      command = "tighten"
    elif j == "-":
      command = "loosen"
    elif j.isalpha():
      letters += j
    amount = n[signLocations[i] + 1:indexList[i] + 1]

  print(letters, command, amount)
