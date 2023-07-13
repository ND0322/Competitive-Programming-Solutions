dpW = [[[[-1] * 31 for i in range(31)] for j in range(31)] for i in range(31)]
dpL = [[[[-1] * 31 for i in range(31)] for j in range(31)] for i in range(31)]

def win(a,b,c,d):

  if dpW[a][b][c][d] == -1:

  
    first = False
    second = False
    third = False
    fourth = False
    fifth = False
    
    if a >= 2 and b >= 1 and d>=2:
      first = lose(a-2,b-1,c,d-2)
    if a>=1 and b >= 1 and c>=1 and d>=1:
      second = lose(a-1,b-1,c-1,d-1)
    if c >= 2 and d >= 1:
      third = lose(a,b,c-2,d-1)
    if b>=3:
      fourth = lose(a,b-3,c,d)
    if a >= 1 and d>=1:
      fifth = lose(a-1,b,c,d-1)
  
  
    if first or second or third or fourth or fifth:
      dpW[a][b][c][d] = True
      
    else:
      dpW[a][b][c][d] = False

  return dpW[a][b][c][d]
    
    
  
def lose(a,b,c,d):

  if dpL[a][b][c][d] == -1:

    if (a < 2 or b < 1 or d < 2) and (a < 1 or b < 1 or c < 1 or d < 1) and (c < 2 or d < 1) and (b < 3) and (a < 1 or d<1):
      
      dpL[a][b][c][d] = True
      return True


    first = True
    second = True
    third = True
    fourth = True
    fifth = True
    
    if a >= 2 and b >= 1 and d>=2:
      first = win(a-2,b-1,c,d-2)
    if a>=1 and b >= 1 and c>=1 and d>=1:
      second = win(a-1,b-1,c-1,d-1)
    if c >= 2 and d >= 1:
      third = win(a,b,c-2,d-1)
    if b>=3:
      fourth = win(a,b-3,c,d)
    if a >= 1 and d>=1:
      fifth = win(a-1,b,c,d-1)
  
    if first and second and third and fourth and fifth:
      dpL[a][b][c][d] = True
  
    else:
      dpL[a][b][c][d] = False

  return dpL[a][b][c][d]
    
      
  
  


  

    

  

n = int(input())


for i in range(n):
  w,x,y,z = map(int,input().split(" "))
  if win(w,x,y,z):
    print("Patrick")
  else:
    print("Roland")
