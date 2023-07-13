n = int(input())


boxes = []
 
for i in range(n):
  boxes.append(sorted(list(map(int,input().split(" ")))))

  

for _ in range(int(input())):
  x,y,z = map(int,sorted(list(map(int,input().split(" ")))))

 


  small = float("inf")
  for i in boxes:

    
    if x > i[0] or y > i[1] or z > i[2]:
      continue
    else:
      if i[0] * i[1] * i[2] < small:
        small = i[0] * i[1] * i[2]
        
        
    
    

  if small == float("inf"):
    print("Item does not fit.")
  else:
    print(small)
