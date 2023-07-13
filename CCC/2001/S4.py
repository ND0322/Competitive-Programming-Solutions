#formula radius = r = a*b*c/ (4 * sqrt(p/2*(p/2 - a)*(p/2-b) * (p/2-c))) where a,b,c are 3 sides of a triangle, and p is perimenter 


n = int(input())

points = []

for i in range(n):
  x,y = map(int,input().split(" "))
  points.append((x,y))


ans = 0
for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      a = (abs(points[i][0]-points[j][0])**2+abs(points[i][1]-points[j][1])**2)**(1/2)
      b = (abs(points[j][0]-points[k][0])**2+abs(points[j][1]-points[k][1])**2)**(1/2)
      c = (abs(points[k][0]-points[i][0])**2+abs(points[k][1]-points[i][1])**2)**(1/2)


      
      s = (a+b+c)/2
      area = (4 * ((s * (s - a) * (s-b) *(s-c))**(1/2)))
      d = 0

      

      if area == 0 or a**2 + b**2 - c**2 < 0 or c**2 + b**2 - a**2 < 0 or a**2 + c**2 - b**2 < 0:
        if a > d:
          d = a
        if b > d:
          d = b
        if c > d:
          d = c
        
        
      else:
        d = (a*b*c)/area*2
      
      if d > ans:
          ans = d

print(round(ans,2))
