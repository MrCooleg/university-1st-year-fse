input_string = 'Введите номер файла: '

#открываем файл
while True:
    # вводим номер файла
    n = int(input(input_string))

    # если файл существует — открываем его и записываем его строки в lines, если нет — просим ввести n заново
    try:
        with open(f'inmap{n}.dat', 'r') as file:
            lines = file.read().splitlines()

        break
    except FileNotFoundError:
        input_string = 'Файл не существует, создайте файл с таким номером или введите другой номер файла: '

#первая строка lines — это 2 числа записанные через пробел (количество мест для посещения и масштаб)
#поэтому делим строку через split() и записываем значения чисел
places = int(lines[0].split()[0])
scale = float(lines[0].split()[1])
#записываем остальные строки в массив строк distances
distances = lines[1:]
total = 0

#считаем сумму всех расстояний
#(берем строку из distances как число float и умножаем на масштаб scale, округляя результат)
for distance in distances:
    total += round(float(distance) * scale, 1)
