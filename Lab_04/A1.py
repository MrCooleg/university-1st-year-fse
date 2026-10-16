import random
import time

#вводим значение с проверкой на корректность ввода
while True:
    try:
        count = int(input('Введите количество примеров: '))
        break
    except ValueError:
        print('Некорректный ввод. Пожалуйста, введите целое число')

#объявляем переменные общего затраченного времени на ответы и количества правильных ответов
total_time = 0
total_correct = 0

#начинаем цикл вопросов
for i in range(count):
    #генерируем два случайных целых числа от 2 до 9
    number_a = random.randint(2, 9)
    number_b = random.randint(2, 9)

    #фиксируем значение времени до ввода ответа
    start_time = time.perf_counter()

    #выводим пример и просим ввести ответ с проверкой на его корректность
    print(f'Вопрос {i + 1}/{count}')

    while True:
        try:
            answer = int(input(f'{number_a} × {number_b} = '))
            break
        except ValueError:
            print(f'Пожалуйста, введите целое число!')

    #получаем промежуток времени, затраченный на ответ и прибавляем его к общей сумме
    delta_time = time.perf_counter() - start_time
    total_time += delta_time

    #выводим ответ и, если он правильный, увеличиваем число верных ответов
    if answer == number_a * number_b:
        print(f'Верно! (Время: {delta_time:.1f} сек)')
        total_correct += 1
    else:
        print(f'Неверно! Правильно: {number_a * number_b} (Время: {delta_time:.1f} сек)')

#считаем среднее арифметическое всех промежутков времени и процент правильных ответов
average_time = total_time / count
correct_percentage = total_correct * 100 / count

#выводим оставшуюся часть
print('=' * 50)
print('СТАТИСТИКА:')
print('=' * 50)
print(f'Общее время: {total_time:.1f} секунд')
print(f'Среднее время на вопрос: {average_time:.1f} сек')
print(f'Правильных ответов: {total_correct}/{count}')
print(f'Процент правильных: {correct_percentage:.1f}%')