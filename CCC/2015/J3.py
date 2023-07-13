word=input()
vowels=["a","e","i","o","u"]
answer = ""
def nextConsonant(letter):
  nextLetter=chr(ord(letter) + 1)
  if letter == "z":
    return "z"
  else:
   if nextLetter not in vowels:
     return nextLetter
   else:
     return chr(ord(nextLetter) + 1)
   
def getclosestVowel(letter):
  closestVowel="a"
  for vowel in vowels:
    if abs(ord(vowel)-ord(letter))< abs(ord(closestVowel)-ord(letter)):
      closestVowel=vowel
  return closestVowel


for i in word:
  if i in vowels:
    answer += i
  else:
    answer += i + getclosestVowel(i) + nextConsonant(i)

print(answer)   



















#print(ord("a"))
#print(chr(97))
