line_number = 1
cat_found =0
while True:
    line = input("Введите строку (или 'СТОП' для завершения): ")
    if line == "СТОП":
        break
    elif "кот" in line.lower():
        cat_found = line_number
        break
    line_number += 1
if cat_found == 0:
    print(-1)
else:
    print(cat_found)

