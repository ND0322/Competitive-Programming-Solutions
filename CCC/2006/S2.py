dict = {}
plain = input()
en = input()
ans = input()

answer = ""

for i in range(0,len(plain)):
  dict[en[i]] = plain[i]

for i in ans:
  if i in dict:
    answer += dict[i]
  else:
    answer += "."
print(answer)
