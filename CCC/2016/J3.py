s = input()

def palindrome(s):
  if len(s) % 2 == 0:

    if s[:len(s) // 2][::-1] == s[len(s)//2:]:
      return True
    return False

  else:
    
    if s[:len(s) // 2][::-1] == s[len(s)//2+1:]:
      return True
    return False


ans = 0
for l in range(len(s)):
  for r in range(l+1,len(s)+1):
    if palindrome(s[l:r]):
      ans = max(ans,r-l)

print(ans)
