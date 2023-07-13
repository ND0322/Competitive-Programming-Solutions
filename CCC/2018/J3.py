x,y,z,w = map(int,input().split(" "))

print(0, x, y + x, z + y + x, x+y+z+w)
print(x,0,y,y+z,y+z+w)
print(x+y,y,0,z,z+w)
print(x+y+z,y+z,z,0,w)
print(x+y+z+w,y+z+w,z+w,w,0)
