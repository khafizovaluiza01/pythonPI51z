first = set()
while True:
    line = input().strip()
    if line == '':
        break
    first.add(line)

second = set()
while True:
    line = input().strip()
    if line == '':
        break
    second.add(line)
common = first.intersection(second)
if common:
    for i in common:
        print(i)
else:
    print('Empty')
