n = float(input())
m = float(input())

bmi = n / (m * m)

if bmi > 25.0:
  print("Overweight")
elif bmi < 18.5:
  print("Underweight")
else:
  print("Normal weight")
