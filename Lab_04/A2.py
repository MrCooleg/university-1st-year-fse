#объявляем методы рисования фигур
def draw_rectangle(rows, cols, char):
    #здесь каждый символ присутствует в каждой позиции матрицы rows x cols,
    #никаких дополнительных условий нет
    for row in range(rows):
        for col in range(cols):
            print(char, end='')
        print()

def draw_triangle(rows, char):
    for row in range(rows):
        #здесь количество символов в строке зависит от номера строки
        for col in range(row + 1):
            print(char, end='')
        print()

def draw_frame(rows, cols, char):
    for row in range(rows):
        for col in range(cols):
            #здесь мы рисуем полную строку символов, если строка первая (индекс = 0),
            #или если строка последняя (индекс = rows - 1),
            #а также рисуем символ, если его позиция первая или последняя (индексы = 0 и cols - 1),
            #иначе рисуем пробел вместо символа
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                print(char, end='')
            else:
                print(' ', end='')
        print()

#вводим значения размеров с проверкой на корректность ввода
while True:
    try:
        n = int(input('Введите количество строк: '))
        break
    except ValueError:
        print('Некорректный ввод. Пожалуйста, введите целое число')

while True:
    try:
        m = int(input('Введите количество столбцов: '))
        break
    except ValueError:
        print('Некорректный ввод. Пожалуйста, введите целое число')

#выводим фигуры
print(f'\nПРЯМОУГОЛЬНИК {n}x{m}:')
draw_rectangle(n, m, '#')

print(f'\nПРАВЫЙ ТРЕУГОЛЬНИК:')
draw_triangle(n, '#')

print(f'\nРАМКА {n}x{m}:')
draw_frame(n, m, '#')