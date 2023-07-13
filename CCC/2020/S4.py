# finshed pypy3 :15/15
class Sec:
  a=0
  b=0
  c=0
  def add(self,charater):
    if charater =="A":
      self.a+=1
    if charater =="B":
      self.b+=1
    if charater =="C":
      self.c+=1
  def remove(self,charater):
    if charater =="A":
      self.a-=1
    if charater =="B":
      self.b-=1
    if charater =="C":
      self.c-=1
  def __str__(self) -> str:
    return "a:"+str(self.a)+"\n"+"b:"+str(self.b)+"\n"+"c:"+str(self.c)+"\n"
# s="CBACA"
                                          
def solve(s):
  n=len(s)
  numberOfA=0
  numberOfB=0
  numberOfC=0
  for i in range(len(s)):
    if s[i]=="A":numberOfA+=1
    if s[i]=="B":numberOfB+=1
    if s[i]=="C":numberOfC+=1
      
  secA=Sec()
  secB=Sec()
  secC=Sec()
  index=0
  for i in range (numberOfA):
    secA.add(s[index])
    index+=1
  for i in range (numberOfB):
    secB.add(s[index])
    index+=1
  for i in range (numberOfC):
    secC.add(s[index])
    index+=1
  minSwap = float("inf")
  
  for i in range(len(s)):
      swap = secA.b+secA.c+secB.a+secB.c-min(secA.b,secB.a)
      if (minSwap>swap): minSwap=swap
      secA.remove(s[i%n])
      secA.add(s[(i+numberOfA)%n])
      secB.remove(s[(i+numberOfA)%n])
      secB.add(s[(i+numberOfA+numberOfB)%n])
      secC.remove(s[(i+numberOfA+numberOfB)%n])
      secC.add(s[(i+numberOfA+numberOfB+numberOfC)%n])
      

  return minSwap
    
  
s= list(input())
abc = solve(s)
for i in range (len(s)):
  if s[i]=="B":
    s[i]="C"
  elif s[i]=="C":
    s[i]="B"
acb= solve(s)
print(min(abc,acb))
