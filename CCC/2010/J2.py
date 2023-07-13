a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())



nikky=(s//(a+b))*(a-b)

if s%(a+b)>a:
    nikky+=(2*a-(s%(a+b)))    
else:
    nikky+=(s%(a+b))    



byron=(s//(c+d))*(c-d)

if s%(c+d)>c:
    byron+=(2*c-(s%(c+d)))    
else:
    byron+=(s%(c+d))  
  
 
if byron == nikky:
    print("Tied")
elif byron > nikky:
    print("Byron")
else:
    print("Nikky")
