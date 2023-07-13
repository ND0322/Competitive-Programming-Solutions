a = int(input())
e = int(input())

ans = []


if a <= 2 and e <= 3:
    ans.append("GraemeMercurian")
if a >= 3 and e <= 4:
    ans.append("TroyMartian")
if a <= 6 and e >= 2:
    ans.append("VladSaturnian")
    
for i in ans:
    print(i)
