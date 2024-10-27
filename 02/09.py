login = input('Логин:')
backup_email = input('Почта: ')

if "@" in login:
  print("Некорректный логин")
elif "@" not in backup_email:
  print("Некорректный адрес")
else:
  print("OK")