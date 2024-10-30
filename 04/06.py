while True:
    pass1 = input("Введите пароль: ")
    pass2 = input("ВВедите пароль повторно:")
    if len(pass1)<8:
        print("короткий")
    elif '123' in pass1:
        print("простой ")
    elif pass1 != pass2:
        print("различаются")
    else:
        print("Ок")
        break

