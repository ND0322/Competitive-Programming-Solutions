a = int(input())
b = int(input())
c = int(input())
d = int(input())


if a == b and b == c and c== d and d == a:
  print("Fish At Constant Depth")
elif a < b < c < d:
  print("Fish Rising")
elif a > b > c > d :
  print("Fish Diving")

else:
  print("No Fish")
