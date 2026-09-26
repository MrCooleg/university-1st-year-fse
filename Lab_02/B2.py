#возьмем функцию округления из решения прошлой задачи и доработаем:
#теперь корректно работает для отрицательных чисел
def school_round(num: float, digits: int) -> float:
    factor = 10 ** digits
    #сдвигаем запятую вправо
    shifted = num * factor
    #прибавляем 0.5 для положительных
    #или вычитаем 0.5 для отрицательных чисел
    if num >= 0:
        rounded = int(shifted + 0.5)
    else:
        rounded = int(shifted - 0.5)
    #возвращаем запятую на место
    return rounded / factor


#введём функцию, которая считает среднее арифметическое
def average(nums: list):
    return sum(nums) / len(nums)


#открываем файл и записываем его строки в lines
with open('1.WCData.txt', 'r') as file1:
    lines = file1.read().splitlines()

time = []
air_temp = []
wind_speed = []

#третья и последующие строки lines — это строка, состоящая из времени (HH:MM:SS) и 2 чисел (Air Temp и Wind Speed)
#внутри одной строки всё записано через пробелы, поэтому делим каждую через split() и записываем значения
for i in range(2, len(lines)):
    time.append(lines[i].split()[0])
    air_temp.append(int(lines[i].split()[1]))
    wind_speed.append(int(lines[i].split()[2]))

wc_temp = []
wc_effect = []

#рассчитываем температуру WC и WC Effect и записываем в соответствующие значения
for i in range(len(time)):
    wc_temp.append(school_round(35.74 + 0.6125 * air_temp[i] + (0.4275 * air_temp[i] - 35.75) * wind_speed[i] ** 0.16, 1))
    wc_effect.append(school_round(wc_temp[i] - air_temp[i], 1))

#создаём файл и записываем в него
with open('1.WindChillReport.txt', 'w', encoding='utf-8') as file2:
    file2.write('Time     WC temp     WC Effect\n')
    file2.write('-' * 30 + '\n')

    #записываем отформатированные строки
    for i in range(len(time)):
        file2.write(time[i] + ' {: 7} {: 13}\n'.format(wc_temp[i], wc_effect[i]))

    #записываем финальную строчку файла, используя среднее арифметическое всех температур
    file2.write('-' * 30 + '\n\n')
    file2.write(
        f'The average adjusted temperature, based on {len(time)} observations, was {school_round(average(wc_temp), 1)}\n')