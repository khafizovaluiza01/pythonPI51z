text = 0
text_max = ''
text_min = ''
while True:
    text = input('Enter a string: ')
    if 'стоп' not in text.lower():
        if text_min == '':
            text_min = text
        if text[1:] > text_max[1:]:
            text_max = text
        if text[1:] < text_min[1:]:
            text_min = text
        print(text_min, text_max)

    else:

        set_max = set(text_max.lower())
        set_min = set(text_min.lower())


        print('да' if set_min.issubset(set_max) else 'нет')
        break