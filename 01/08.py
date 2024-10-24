def main():
    # Считываем данные пользователя
    FirstName = input("Введите ваше имя: ")
    LastName = input("Введите вашу фамилию: ")
    FavoriteAnimal = input("Введите ваше любимое животное: ")
    ZodiacSign = input("Введите ваш знак зодиака: ")

    # Формируем и выводим гороскоп
    horoscope = (
        f"Индивидуальный гороскоп для пользователя {FirstName} {LastName}\n"
        f"Кем вы были в прошлой жизни: {FavoriteAnimal}\n"
        f"Ваш знак зодиака - {ZodiacSign}, поэтому вы - тонко чувствующая натура."
    )

    print(horoscope)

if __name__ == "__main__":
    main()
