low = 1
high = 1000

for i in range(10):
    count = (low + high) // 2
    print(f"я думаю загаданное число {count}")
    symbol = input("Введите знак: ")

    if symbol == '>':
        high = count-1
    elif symbol == '<':
        low = count+1
    elif symbol == '=':
        print(f"я угадал {i+1} попыток")
        break
    else:
        print("неверный ввод.")
        break
if symbol != '=':
    print("я не смог угадать.")