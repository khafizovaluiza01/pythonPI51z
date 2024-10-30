pass1 = input("Введите пароль: ")
pass2 = input("ВВедите пароль повторно:")
if len(pass1) < 8:
    print("Короткий ")
elif pass1 != pass2:
    print("Различаются")
else:
    print('Оk')
