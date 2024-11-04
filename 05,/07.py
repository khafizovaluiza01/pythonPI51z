num = int(input('Enter a number: '))
iner = []
for i in range(1,num+1):
    if num % i ==0:
        iner.append(i)
print(*iner)
if len(iner)==2:
    print('Простое')
else:
    print("Нет")


