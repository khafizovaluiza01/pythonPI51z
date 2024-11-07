text_max = ''
text_min = ''
while True:
    text = input('Enter a string: ')
    if 'стоп' not in text.lower():
        if text_min == '':
            text_min = text
        if len(text) > len(text_max):
            text_max = text
        if len(text) < len(text_min):
            text_min = text

    else:

        set_max = set(text_max.lower())
        set_min = set(text_min.lower())

        print('да' if set_min.issubset(set_max) else 'нет')
        break