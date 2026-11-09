#проверяем введённую строку
def is_valid(string):
    return string.isdigit() and len(string) in [13, 15, 16]

#вычисляем сумму по алгоритму Луна
def get_sum(string):
    sum = 0
    rev_string = string[::-1]

    for i in range(1, len(rev_string), 2):
        offset = 9 if int(rev_string[i]) * 2 > 9 else 0
        sum += int(rev_string[i]) * 2 - offset

    for i in range(0, len(rev_string), 2):
        sum += int(rev_string[i])

    return sum

#проверяем, корректна ли сумма
def is_valid_sum(sum):
    return sum % 10 == 0

#получаем тип карты
def get_card(string):
    if (len(string) == 13 or len(string) == 16) and string.startswith('4'):
        return 'Visa'
    if len(string) == 15 and (string.startswith('34') or string.startswith('37')):
        return 'American Express'
    if len(string) == 16 and any(string.startswith(str(num)) for num in range(51, 56)):
        return 'MasterCard'

    return 'Неизвестная карта'

#просим ввести номер карты
while True:
    card_number = input('Введите номер карты: ')

    #если строка не прошла проверки, просим ввести заново
    if not is_valid(card_number):
        print('Некорректный ввод')
    else:
        break

#если номер карты существует и карта является картой известного нам типа, то выводим ответ
if is_valid_sum(get_sum(card_number)):
    if get_card(card_number) != 'Неизвестная карта':
        print(f'Карта с номером {card_number} является картой {get_card(card_number)}')
    else:
        #если карта неизвестна, то вывод так и скажет
        print(get_card(card_number))
else:
    #иначе, карты не существует
    print(f'Карты с номером {card_number} не существует')