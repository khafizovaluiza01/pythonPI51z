n= int(input('Enter a number: '))

total_iq = 0
iq_list = []

for i in range(n):
  iq = int(input())
  total_iq += iq
  iq_list.append(iq)

  if i == 0:
    print("0")
  else:
    average_iq = total_iq / (i + 1)
    if iq > average_iq:
      print(">")
    elif iq < average_iq:
      print("<")
    else:
      print("0")