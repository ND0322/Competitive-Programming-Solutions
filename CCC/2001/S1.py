s = input()

ans = 0


print("Cards Dealt Points")

clubs = s[s.index("C") + 1:s.index("D")]
diamonds = s[s.index("D") + 1:s.index("H")]
hearts = s[s.index("H") + 1:s.index("S")]
spades = s[s.index("S") + 1:]

deck = [clubs,diamonds,hearts,spades]


for i in range(len(deck)):
  curAns = 0
  toP = ""

  if i == 0:
    toP += "Clubs "
  if i == 1:
    toP += "Diamonds "
  if i == 2:
    toP += "Hearts "
  if i == 3:
    toP += "Spades "
    
  if len(deck[i]) == 0:
    curAns += 3
  if len(deck[i]) == 1:
    curAns += 2
  if len(deck[i]) == 2:
    curAns += 1

  for card in deck[i]:
    if card == 'A':
      curAns += 4
    if card == "K":
      curAns += 3
    if card == "Q":
      curAns += 2
    if card == "J":
      curAns += 1

    toP += card + " "
  toP += str(curAns)
  ans += curAns

  print(toP)
print("   Total " + str(ans))
