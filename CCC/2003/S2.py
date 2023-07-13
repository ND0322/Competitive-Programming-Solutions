vowels = ["a","e","i","o","u"]


for _ in range(int(input())):
  

  
  first = input().split(" ")[-1].lower()
  second = input().split(" ")[-1].lower()
  third = input().split(" ")[-1].lower()
  fourth = input().split(" ")[-1].lower()

  for i in range(len(first)-1,-1,-1):
    if first[i] in vowels:
      first = first[i:]
      break
  for i in range(len(second) -1,-1,-1):
    if second[i] in vowels:
      second = second[i:]
      break
  for i in range(len(third) -1,-1,-1):
    if third[i] in vowels:
      third = third[i:]
      break
  for i in range(len(fourth) -1,-1,-1):
    if fourth[i] in vowels:
      fourth = fourth[i:]
      break


  if first == second and second == third and third == fourth and fourth == first:
    print("perfect")
  elif first == second and third == fourth:
    print("even")
  elif first == third and second == fourth:
    print("cross")
  elif first == fourth and second == third:
    print("shell")
  else:
    print("free")
