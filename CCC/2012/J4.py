k = int(input())
word = input()
ans = ""
for i in range(0,len(word)):
  s = 3* (i+1) + k

 
  if ord(word[i]) - s > 64:
    
    ans += chr(ord(word[i]) - s)
  else:
    ans += chr(90 - (s - (ord(word[i]) - 64) )) 

print(ans)
