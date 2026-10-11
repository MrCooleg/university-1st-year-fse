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
    #если команда P, то выводим текущее состояние игры:
    elif command == 'P':
        #добавляем в список строк для вывода пустую строчку, с которой будем дальше работать
        output.append('')

        if cat_row != '' and cat_col != '' and mouse_row != '' and mouse_col != '':
            #вычисляем расстояние между котом и мышью
            distance_row = abs(cat_row - mouse_row) + 1  #разница между ординатами кота и мыши, увеличенная на 1
            distance_col = abs(cat_col - mouse_col) + 1  #разница между абсциссами кота и мыши, увеличенная на 1
            distance = distance_row + distance_col - 2  #сумма размеров прямоугольника, уменьшенная на 2
            distance = f'{distance: >{len(str(rows + cols - 2))}}' #форматируем с выравниванием справа
        else:
            distance = ''

        #инициализируем список значений в ячейках таблицы:
        #проверяем, известна ли начальная позиция кота:
        #если да — выравниваем число справа относительно самого большого числа под или над этим;
        #если нет — представляем число как знак вопроса и делаем то же самое
        if cat_row == '':
            cat_row_str = f'{'?': >{len(str(rows))}}'
        else:
            cat_row_str = f'{cat_row: >{len(str(rows))}}'
        if cat_col == '':
            cat_col_str = f'{'?': >{len(str(cols))}}'
        else:
            cat_col_str = f'{cat_col: >{len(str(cols))}}'

        #проверяем, известна ли начальная позиция мыши, форматируем так же
        if mouse_row == '':
            mouse_row_str = f'{'?': >{len(str(rows))}}'
        else:
            mouse_row_str = f'{mouse_row: >{len(str(rows))}}'
        if mouse_col == '':
            mouse_col_str = f'{'?': >{len(str(cols))}}'
        else:
            mouse_col_str = f'{mouse_col: >{len(str(cols))}}'

        #для форматирования таблицы, где каждая ячейка выравнивается по центру, задаём список со значениями ячеек
        column_values = [f'({cat_row_str},{cat_col_str})', f'({mouse_row_str},{mouse_col_str})', str(distance)]

        #форматируем таблицу: содержимое каждого столбца таблицы выровнено по центру
        for j in range(len(column_values)):
            output[k] += f'{column_values[j]: ^{column_max_len[j]}}'

            if j == 0:
                output[k] += ' ' * 5 #отступ между ячейками 1 и 2 — 5 пробелов
            elif j == 1:
                output[k] += ' ' * 3 #отступ между ячейками 2 и 3 — 3 пробела
            else:
                output[k] += '\n' #в конце строки дописываем переход на новую строку

        #увеличиваем индекс для следующей строки
        k += 1

#рисуем вторую черту
output.append('-' * (len(output[2]) - 1) + '\n' * 3)

#форматируем вторую таблицу:
#каждая ячейка выровнена справа с отступом в 4 пробела между ячейками
column_max_len = []
column_names = ['Distance', 'Mouse', 'Cat']
column_values = ['', str(mouse_path), str(cat_path)]

output.append('')
output.append('')
k += 2

#каждый столбец форматируем как раньше
for j in range(len(column_names)):
    column_max_len.append(max(len(column_names[j]), len(column_values[j])))
    output[k - 1] += f'{column_names[j]: >{column_max_len[j]}}'
    output[k] += f'{column_values[j]: >{column_max_len[j]}}'

    if j == 0:
        output[k - 1] += ' ' * 3 #отступы между ячейками 1 и 2 в этой и следующей строке — 3 пробела
        output[k] += ' ' * 3
    elif j == 1:
        output[k - 1] += ' ' * 4 #отступы между ячейками 2 и 3 в этой и следующей строке — 4 пробела
        output[k] += ' ' * 4
    else:
        output[k - 1] += '\n' #конец строки — переводим на следующую
        output[k] += '\n\n' #конец строки — переводим на следующую и пропускаем еще одну строку

#финальная строчка вывода с исходом игры
if cat_row != '' and cat_col != '' and mouse_row != '' and mouse_col != '':
    if cat_row == mouse_row and cat_col == mouse_col:
        output.append(f'Mouse caught at: ({mouse_row: >{len(str(rows))}},{mouse_col: >{len(str(cols))}})\n')
    else:
        output.append('Mouse evaded Cat\n')

#создаём файл и записываем каждую строку из списка для вывода в него
with open(f'{n}.PursuitLog.txt', 'w', encoding='utf-8') as file2:
    for line in output:
        file2.write(line)