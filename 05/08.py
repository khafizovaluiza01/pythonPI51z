from time import sleep

n = int(input('Enter a number: '))
if n >= 0:
    for i in range(n,-1,-1):
        print('Осталось секунд: ', i)
        sleep(1)
    print('Пуск')
else:
    print('Пуск')