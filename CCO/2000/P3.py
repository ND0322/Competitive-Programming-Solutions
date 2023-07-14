dpW = [[[[[[[-1] * 32 for i in range(5)] for j in range(5)] for k in range(5)] for l in range(5)] for m in range(5)] for n in range(5)]
dpL = [[[[[[[-1] * 32 for i in range(5)] for j in range(5)] for k in range(5)] for l in range(5)] for m in range(5)] for n in range(5)]




def win(a,b,c,d,e,f,tot):

  if dpW[a][b][c][d][e][f][tot] == -1:

    if tot == 31:
      dpW[a][b][c][d][e][f][tot] = False
      return False
  
  
  
    one = False
    two = False
    three = False
    four = False
    five = False
    six = False
  
    if a > 0 and tot + 1 <= 31:
      one = lose(a-1,b,c,d,e,f,tot+1)
    if b > 0 and tot + 2 <= 31:
      two = lose(a,b-1,c,d,e,f,tot+2)
    if c > 0 and tot + 3 <= 31:
      three = lose(a,b,c-1,d,e,f,tot+3)
    if d > 0 and tot + 4 <= 31:
      four = lose(a,b,c,d-1,e,f,tot+4)
    if e > 0 and tot + 5 <= 31:
      five = lose(a,b,c,d,e-1,f,tot+5)
    if f > 0 and tot + 6 <= 31:
      six = lose(a,b,c,d,e,f-1,tot+6)
  
    if one or two or three or four or five or six:
      dpW[a][b][c][d][e][f][tot] = True
  
    else:
  
      dpW[a][b][c][d][e][f][tot] =False


  
  return dpW[a][b][c][d][e][f][tot]
    

def lose(a,b,c,d,e,f,tot):

  if dpL[a][b][c][d][e][f][tot] == -1:

    if tot == 31:
      dpL[a][b][c][d][e][f][tot] = True
      return True
  
  
  
  
  
    check = True
    cards = [a,b,c,d,e,f]
  
    for i in range(6):
      if cards[i] <= 0:
        continue
      if tot + i+1 > 31:
        continue
      check = False
      break
  
    if check:
      dpL[a][b][c][d][e][f][tot] = True
      return True
  
    one = True
    two = True
    three = True
    four = True
    five = True
    six = True
  
    if a > 0 and tot + 1 <= 31:
      one = win(a-1,b,c,d,e,f,tot+1)
    if b > 0 and tot + 2 <= 31:
      two = win(a,b-1,c,d,e,f,tot+2)
    if c > 0 and tot + 3 <= 31:
      three = win(a,b,c-1,d,e,f,tot+3)
    if d > 0 and tot + 4 <= 31:
      four = win(a,b,c,d-1,e,f,tot+4)
    if e > 0 and tot + 5 <= 31:
      five = win(a,b,c,d,e-1,f,tot+5)
    if f > 0 and tot + 6 <= 31:
      six = win(a,b,c,d,e,f-1,tot+6)
  
  
    if one and two and three and four and five and six:
      dpL[a][b][c][d][e][f][tot] = True
      
    else:
      
      dpL[a][b][c][d][e][f][tot] = False
      
  return dpL[a][b][c][d][e][f][tot]

  
  
    

      
    

  

  

for _ in range(int(input())):
  

  cards = [4] * 7
  c = list(input())

  e = 0
  for i in c:
    cards[int(i)] -=1
    e += int(i)

  if len(c) % 2 == 0:
    if win(cards[1],cards[2],cards[3],cards[4],cards[5],cards[6],e):
      print("A")
    else:
      print("B")
  else:
    if win(cards[1],cards[2],cards[3],cards[4],cards[5],cards[6],e):
      print("B")
    else:
      print("A")
