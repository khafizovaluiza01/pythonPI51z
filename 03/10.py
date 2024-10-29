num_first = float(input('Enter first number: '))
num_two = float(input('Enter second number: '))
math_operator = str(input('Enter math operator: '))

if math_operator == "+":
  print(num_first + num_two)
elif math_operator == "-":
  print(num_first - num_two)
elif math_operator == "*":
  print(num_first * num_two)
elif math_operator == "/" and num_two != 0:
  print(num_first / num_two)
else:
  print("888888")