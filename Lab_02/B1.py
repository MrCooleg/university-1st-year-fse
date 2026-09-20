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

#выводим
print('Dikevich Egor')
print('Simple Map Distance Computations\n')
#так как число scale это число от 0.00 до 1000.00 (два символа после запятой), то форматируем строку,
#чтобы число в строке всегда занимало одну и ту же ширину в символах
print('Map Scale Factor: {: 7} miles per inch\n'.format(scale))
print('      Map       Mileage')
print('      Measure   Distance')
print('=' * 60)

#выводим каждую строку таблицы, форматируя её так, чтобы помещались числа
#i + 1 (номер места), distance (Map Measure) и distance * scale (Mileage Distance)
#максимальная длина 1-го числа — 3 символа (количество мест от 0 до 100 штук, 100 — это 3 символа)
#максимальная длина 2-го числа — 6 символов (расстояние на карте от 0.0 до 1000.0 дюймов, 1000.0 — это 6 символов)
#максимальная длина 3-го числа — 9 символов (distance * scale от 0.0 до 1000000.0 миль, 1000000.0 — это 9 символов)
for i in range(places):
    distance = float(distances[i])
    print('#{: 3} {: 6} {: 9}'.format(i + 1, distance, round(float(distance) * scale, 1)))

#выводим сумму расстояний
print('=' * 60)
print(f'Total Distance:    {total} miles')