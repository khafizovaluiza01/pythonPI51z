print("Вы находитесь в темном лесу. Перед вами развилка. Вы можете пойти 'вперед', 'налево' или 'направо'. Введите одно из слов в кавычках для выбора.")

choice = input()

if choice == "вперед":
    print("Вы идете вперед по узкой тропинке, которая ведет к большой поляне. На поляне стоит маленький домик с дымящейся трубой. Вы можете 'зайти в дом' или 'обойти его'. Введите одно из слов в кавычках для выбора.")

    choice2 = input()
    if choice2 == "зайти в дом":
        print("Вы заходите в дом и вас встречает приветливый старик. Он предлагает вам чаю и угощения. Вы проводите время в уютном доме, наслаждаясь гостеприимством. Вы спаслись!")
    elif choice2 == "обойти его":
        print("Вы решаете обойти дом. Но, когда вы проходите мимо него, из-за угла выпрыгивает огромный волк и утаскивает вас в лес. Вы погибли.")
    else:
        print("Ошибка: Некорректный выбор. Игра завершена.")

elif choice == "налево":
    print("Вы поворачиваете налево и оказываетесь у заброшенной шахты. Вы видите узкий проход, ведущий вглубь шахты. Вы можете 'войти в шахту' или 'остаться снаружи'. Введите одно из слов в кавычках для выбора.")

    choice2 = input()
    if choice2 == "войти в шахту":
        print("Вы спускаетесь в шахту. Внизу вы находите клад - сундук с золотом! Вы богаты! Вы спаслись!")
    elif choice2 == "остаться снаружи":
        print("Вы решаете не рисковать и остаться снаружи. Вы возвращаетесь на развилку и решаете идти другим путем. Вы спаслись, но не разбогатели.")
    else:
        print("Ошибка: Некорректный выбор. Игра завершена.")

elif choice == "направо":
    print("Вы поворачиваете направо и оказываетесь на берегу реки. Вы можете 'перейти реку вброд' или 'попытаться найти брод'. Введите одно из слов в кавычках для выбора.")

    choice2 = input()
    if choice2 == "перейти реку вброд":
        print("Вы решаете перейти реку вброд. Но вода оказывается очень холодной и быстрой. Вы тонете. Вы погибли.")
    elif choice2 == "попытаться найти брод":
        print("Вы начинаете искать брод. Вам удается найти узкий перекат и перейти на другой берег. Вы спаслись!")
    else:
        print("Ошибка: Некорректный выбор. Игра завершена.")

else:
    print("Ошибка: Некорректный выбор. Игра завершена.")