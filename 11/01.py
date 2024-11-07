n = int(input('Enter a number: '))
numbers = []

for i in range(n):
    numbers.append(int(input('Enter a number list: ')))

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