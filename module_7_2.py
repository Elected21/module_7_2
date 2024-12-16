def custom_write(file_name, strings):
    strings_positions = {}
    line_counter = 1

    file = open(file_name, 'w', encoding='utf-8')

    for i in strings:
        key = (line_counter, file.tell())
        value = f'{i}'
        strings_positions.update({key: value})
        file.write(f'{i}\n')
        line_counter += 1
    file.close()
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)