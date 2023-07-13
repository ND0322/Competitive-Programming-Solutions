lim = int(input())
sp = int(input())

if sp - lim >= 1 and sp - lim <= 20:
  print("You are speeding and your fine is $100.")
elif sp - lim >= 21 and sp - lim <= 30:
  print("You are speeding and your fine is $270.")
elif sp - lim >= 31:
  print("You are speeding and your fine is $500.")
else:
  print("Congratulations, you are within the speed limit!")
