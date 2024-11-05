n = int(input('Enter a number: '))
total = False
for i in range(1, n+1):
    word = str(input('Enter a word: '))
    if "Кот" in word or "кот" in word:
        total = True
if total:
    print('Мяу')
else:
    print('Нет')