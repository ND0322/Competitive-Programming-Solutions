n = int(input())

ch = {}
for i in range(n):
  x,y = input().split(" ")
  ch[y] = x

s = input()
i = 0
ans = ""
while i < len(s):
  
  for key in ch:
    if i + len(key) <= len(s):
      
      if s[i:i+len(key)] == key:
        
        ans += ch[key]
        i = i+len(key)

print(ans)
