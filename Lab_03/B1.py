input_string = 'Введите номер файла: '

# открываем файл
while True:
    # вводим номер файла
    n = int(input(input_string))

    # если файл существует — открываем его и записываем его строки в lines, если нет — просим ввести n заново
    try:
        with open(f'{n}.ChaseData.txt', 'r') as file1:
            lines = file1.read().splitlines()

        break
    except FileNotFoundError:
        input_string = f'Файл {n}.ChaseData.txt не существует, создайте этот файл или введите другой номер файла: '

#задаём сетку размером rows x cols (кол-во строк на кол-во столбцов)
rows = int(lines[0].split()[0])
cols = int(lines[0].split()[1])

#сразу записываем в список строк для вывода первую строку
output = ['Cat and Mouse\n\n']

#для форматирования таблицы, где каждая ячейка выравнивается по центру, задаём списки с названиями
#столбцов и значениями ячеек, чтобы для каждого столбца найти максимальную длину строки
column_names = ['Cat', 'Mouse', 'Distance']
column_values = [f'({rows},{cols})', f'({rows},{cols})', str(rows + cols - 2)] #так как расстояние между
#котом и мышью — это сумма длины и ширины прямоугольника, в противоположных углах которого находятся
#кот и мышь, уменьшенная на 2, то максимальное значение расстояния между ними — это сумма размеров сетки,
#уменьшенная на 2

#задаём список максимальных длин каждой строки, чтобы рассчитать их сразу и потом только использовать для
#форматирования каждой строки таблицы
column_max_len = []

#добавляем в список строк для вывода пустую строчку, с которой будем дальше работать
output.append('')

#для каждого столбца ищем максимальную длину строки и используем её для форматирования таблицы,
#название каждого столбца таблицы выровнено по центру
for j in range(len(column_names)):
    column_max_len.append(max(len(column_names[j]), len(column_values[j])))
    output[1] += f'{column_names[j]: ^{column_max_len[j]}}'

    if j == 0:
        output[1] += ' ' * 5 #отступ между ячейками 1 и 2 — 5 пробелов
    elif j == 1:
        output[1] += ' ' * 3 #отступ между ячейками 2 и 3 — 3 пробела
    else:
        output[1] += '\n' #в конце строки дописываем переход на новую строку

#рисуем черту длиной в предыдущую строчку (символ \n в предыдущей строке не учитываем)
output.append('-' * (len(output[1]) - 1) + '\n')

#задаём переменную индекса в списке строк для вывода, в списке уже есть строки с индексами 0, 1 и 2,
#значит следующая строка будет с индексом 3 и так далее
k = 3

#инициализируем переменные положения кота и его пройденного пути
cat_row = ''
cat_col = ''
cat_path = 0

#инициализируем переменные положения мыши и её пройденного пути
mouse_row = ''
mouse_col = ''
mouse_path = 0

#проходим по оставшимся строкам файла
for i in range(1, len(lines)):
    #проверяем, равны ли координаты между собой, если да — принудительно выходим из цикла (кот поймал мышь)
    if cat_row != '' and cat_col != '' and mouse_row != '' and mouse_col != '':
        if cat_row == mouse_row and cat_col == mouse_col:
            break

    #считываем команду
    command = lines[i].split()[0]

    #если команда C, то работаем с котом:
    if command == 'C':
        #записываем ход кота по вертикали и горизонтали
        r_path = int(lines[i].split()[1])
        c_path = int(lines[i].split()[2])

        #считаем пройденное на этом ходу расстояние и прибавляем в сумму
        if cat_row != '' and cat_col != '':
            cat_path += abs(r_path) + abs(c_path)

        #прибавляем перемещение по каждой оси к положению в этой оси
        if cat_row == '':
            cat_row += str(r_path)
        else:
            cat_row += r_path

        if cat_col == '':
            cat_col += str(c_path)
        else:
            cat_col += c_path

        cat_row = int(cat_row)
        cat_col = int(cat_col)

        #если вышли за рамку, то перемещаемся так, как сказано в условии
        while cat_row <= 0:
            cat_row += rows
        while cat_row > rows:
            cat_row -= rows

        while cat_col <= 0:
            cat_col += cols
        while cat_col > cols:
            cat_col -= cols
    #если команда M, то работаем с мышью:
    elif command == 'M':
        #записываем ход мыши по вертикали и горизонтали
        r_path = int(lines[i].split()[1])
        c_path = int(lines[i].split()[2])

        #считаем пройденное на этом ходу расстояние и прибавляем в сумму
        if mouse_row != '' and mouse_col != '':
            mouse_path += abs(r_path) + abs(c_path)

        #прибавляем перемещение по каждой оси к положению в этой оси
        if mouse_row == '':
            mouse_row += str(r_path)
        else:
            mouse_row += r_path

        if mouse_col == '':
            mouse_col += str(c_path)
        else:
            mouse_col += c_path

        mouse_row = int(mouse_row)
        mouse_col = int(mouse_col)

        #если вышли за рамку, то перемещаемся так, как сказано в условии
        while mouse_row <= 0:
            mouse_row += rows
        while mouse_row > rows:
            mouse_row -= rows

        while mouse_col <= 0:
            mouse_col += cols
        while mouse_col > cols:
            mouse_col -= cols
