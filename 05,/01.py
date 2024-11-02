weather = 0
num = 0
while True:
    if weather < 22.0:
        weather = float(input("Enter a weather: "))
        num += 1
    else:
        break
print(num//7)