e = input()
v = 0
h = 0
for i in e:
  if i == "V":
    v += 1
  else:
    h += 1
v = v % 2
h = h % 2

if h != 0 and v == 0:
  print("3 4" + "\n" + "1 2")
elif h == 0 and v != 0:
  print("2 1" + "\n" + "4 3")
elif h == 0 and v == 0:
  print("1 2" + "\n" + "3 4")
else:
  print("4 3" + "\n" + "2 1")
