n = int(input('Enter a number: '))
numbers = tuple(int(input('Enter a number list: ')) for _ in range(n)) # Используем генератор списка, чтобы создать кортеж

target_number = int(input())
found = False

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] * numbers[j] == target_number:
            found = True
            break

if found:
    print("ДА")
else:
    print("НЕТ")