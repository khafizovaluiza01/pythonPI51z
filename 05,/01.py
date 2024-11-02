weather = 0
num = 0
while True:
    if weather < 22.0:
        weather = float(input("Enter a weather: "))
        num += 1
        print(num)
    else:
        break
print(num//7)