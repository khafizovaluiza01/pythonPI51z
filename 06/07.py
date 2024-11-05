war_state = "Евразия"
peace_state = "Остазия"
N = int(input("Введите количество команд: "))
for _ in range(N):
    command = input().strip()

    if command == "С кем война?":
        print(war_state)
    elif command == "С кем мир?":
        print(peace_state)
    elif command == "Меняем":

        war_state, peace_state = peace_state, war_state