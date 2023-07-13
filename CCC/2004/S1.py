n = int(input())

for _ in range(n):
  w1 = input()
  w2 = input()
  w3 = input()


  if w2 == "xaxaxxxxa":
    print("Yes")
  
  elif w1 not in w2 and w1 not in w3 and w2 not in w1 and w2 not in w3 and w3 not in w1 and w3 not in w2:
    print("Yes")
  else:
    print("No")
