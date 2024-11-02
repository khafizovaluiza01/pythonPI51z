#weather = 0
#num = 0
#while True:
    #if weather < 22.0:
        #weather = float(input("Enter a weather: "))
        #num += 1
        #print(num)
    #else:
        #break
#print(num//7)

days = int(input('Дни: '))
count = 0
for i in range(1, days):
    weather = float(input("Enter a weather: "))
    if weather < 22.0:
        print(weather)
        count +=1
    else:
        print(count //7)
        break
print('Наблюдения завершены! Количество недель составляет: ', count//7)