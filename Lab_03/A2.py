#подключаем модуль string для дальнейшего автоматического задания набора допустимых символов
import string

#задаём строчку allowed, которая состоит из всех допустимых символов, а затем просим ввести пароль
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
password = input('Введите пароль: ')

#проверяем длину пароля и символы пароля и выводим результаты проверок
if len(password) != 8:
    print('Длина пароля не равна 8')

if not any(symbol in string.ascii_uppercase for symbol in password):
    print('В пароле отсутствуют заглавные буквы')

if not any(symbol in string.ascii_lowercase for symbol in password):
    print('В пароле отсутствуют строчные буквы')

if not any(symbol in string.digits for symbol in password):
    print('В пароле отсутствуют цифры')

if not any(symbol in '*-#' for symbol in password):
    print('В пароле отсутствуют специальные символы')

if not all(symbol in allowed for symbol in password):
    print('В пароле используются непредусмотренные символы')