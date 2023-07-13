a = list(map(int,input().split(":")))
min = a[0] * 60 + a[1]

counter=0 # 120/20=6

while(counter < 6):
  #if you are in rush hour 7:00-10:00
  if (420<=min and min<=600):
    #if you are close to the end of rush
    if min+40>600:
      min=600+(40-(600-min))//2
    else:
      min+=40
  #if you are in rush hour 15:00-19:00    
  elif (900<=min and min<=1140):
    if min+40>1140:
      min=1140+(40-(1140-min))//2
    else:
      min+=40
  else:
    min+=20
  counter+=1

min%=1440
h = min//60
m = min%60

if len(str(abs(h))) == 1:
  if len(str(abs(m))) == 1:
    print("0"+str(h)+":"+"0"+str(m))
  else:
    print("0"+str(h)+":"+str(m))
else:
  if len(str(abs(m))) == 1:
    print(str(h)+":"+"0"+str(m))
  else:
    print(str(h)+":"+str(m))
