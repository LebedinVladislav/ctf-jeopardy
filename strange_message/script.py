# код для извлечения закодированного сообщения
# для декодирования можно использовать любой онлайн декодер морзе в текст

with open('message.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        code = ''.join([i for i in line if i in ['-', '.']])
        print(code, end=' ')