a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
c = list(map(int,input().split(" ")))
d = list(map(int,input().split(" ")))


if sum(a) == sum(b) and sum(c) == sum(a) and sum (d) == sum(a):
  if a[0]+b[0]+c[0]+d[0] == a[1]+b[1]+c[1]+d[1] and a[0]+b[0]+c[0]+d[0] == a[2]+b[2]+c[2]+d[2] and a[0]+b[0]+c[0]+d[0] == a[3]+b[3]+c[3]+d[3]:
    if a[0]+b[0]+c[0]+d[0] == sum(a):
      print("magic")
    else:
      print("not magic")
  else:
    print("not magic")
else:
  print("not magic")
