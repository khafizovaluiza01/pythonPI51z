total_sum = 0
count = 0
while True:
    number = int(input("Введите целое число (ноль для остановки): "))
    if number == 0:
        break
    total_sum += number
    count += 1
    if total_sum == 10:
        print(count)
        break
