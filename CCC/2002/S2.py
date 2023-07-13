from fractions import Fraction

top = int(input())
bottom = int(input())





whole = top // bottom

top = top % bottom


fract = Fraction(top,bottom)

top = fract.numerator
bottom = fract.denominator






if whole > 0:
  if top == 0:
    print(whole)
  else:
    print(str(whole), str(top) +"/" +str(bottom))
else:
  if top == 0:
    print(0)
  else:
    print(str(top) + "/" + str(bottom))
