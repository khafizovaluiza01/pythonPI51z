num_count = 1
for i in range(6):
    num = int(input('Enter a number: '))
    if num !=0:
        num_count *=abs(num)
print(num_count)