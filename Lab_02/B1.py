#открываем файл и записываем его строки в lines
with open('inmap0.dat', 'r') as file:
    lines = file.read().splitlines()

#первая строка lines — это 2 числа записанные через пробел (кол-во мест для посещения и масштаб)
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