number = float(input())

if abs(number) < 1e-6:
  print(1e6)
else:
  print(1 / number)