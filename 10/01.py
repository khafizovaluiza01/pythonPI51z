num = int(input('Enter a number: '))
name_list = []
for i in range(1, num+1):
    name =input('Enter a name: ')
    name_list.append(name)
print('\n'.join(name_list))
