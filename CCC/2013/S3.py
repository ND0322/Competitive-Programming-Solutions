t = int(input())
g = int(input())
tList = [0,0,0,0]
gList = ["1 2","1 3","1 4","2 3","2 4","3 4"]
for i in range(g):
  g = input().split(" ")

  #remove the games that already play
  if int(g[0])<int(g[1]):
    gList.remove(g[0]+" "+g[1])
  else:
    gList.remove(g[1]+" "+g[0])


  if int(g[2]) > int(g[3]):
    tList[int(g[0]) - 1] += 3
  elif int(g[2]) < int(g[3]):
    tList[int(g[1]) - 1] += 3
  else:
    tList[int(g[1]) - 1] += 1
    tList[int(g[0]) - 1] += 1
   


#TODO: write a function return true if your fav team winner, otherwise return False
#teams=[10,28,3,19] favTeam ->False


def checkFav(teams, favTeam):
  for i in range(len(teams)):
    if teams[i] >= teams[favTeam - 1] and i != favTeam - 1:
      return False
  return True



#TODO
#remainGame=["1 4","2 3"]

##scores=[1,2,6,1]
#teams[favTeam - 1]


points = [[0,3],[3,0],[1,1]] 
answer=0 #total possible cases
def calPossible(remainGame, scores, favTeam):
  global answer
  #print(scores)
  if len(remainGame)==0:
    if checkFav(scores,favTeam):
      answer+=1
    return;
  else:
    team1=int(remainGame[0][0])-1
    team2 =int(remainGame[0][2])-1
    for i in range (len(points)):
      scores[team1]=scores[team1]+points[i][0]
      scores[team2]=scores[team2]+points[i][1]
      calPossible(remainGame[1:],scores,favTeam)
      scores[team1]=scores[team1]-points[i][0]
      scores[team2]=scores[team2]-points[i][1]




calPossible(gList,tList,t)  
print(answer)
