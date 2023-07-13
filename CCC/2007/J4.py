w1 = {}
w2 = {}

s1 = input().replace(" ","")
s2 = input().replace(" ","")



if len(s1) != len(s2):
  print("Is not an anagram.")
else:
  for i in range(len(s1)):
    if s1[i] not in w1:
      w1[s1[i]] = 1
    else:
      w1[s1[i]] += 1

    if s2[i] not in w2:
      w2[s2[i]] = 1
    else:
      w2[s2[i]] += 1

  check = True

  
  for i in w1:
    if i not in w2:
      print("Is not an anagram.")
      check = False
      break

    if w2[i] != w1[i]:
      print("Is not an anagram.")
      check = False
      break

  if check:
    print("Is an anagram.")
