
n = int(input('Enter a number > 0: '))
if n < 0:
    print('Меньше нуля')
else:
    total = 0

    for i in range(1, n+1):
        num = int(input(f"Enter a number {i}: "))
        if i % 2 == 0:
            total -= num
        else:
            total += num
    print(total)