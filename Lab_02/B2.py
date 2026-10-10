#введём функцию, которая считает среднее арифметическое
def average(nums: list):
    return sum(nums) / len(nums)

input_string = 'Введите номер файла: '

# открываем файл
while True:
    # вводим номер файла
    n = int(input(input_string))

    # если файл существует — открываем его и записываем его строки в lines, если нет — просим ввести n заново
    try:
        with open(f'{n}.WCData.txt', 'r') as file1:
            lines = file1.read().splitlines()

        break
    except FileNotFoundError:
        input_string = 'Файл не существует, создайте файл с таким номером или введите другой номер файла: '

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
    wc_temp.append(round(35.74 + 0.6125 * air_temp[i] + (0.4275 * air_temp[i] - 35.75) * wind_speed[i] ** 0.16, 1))
    wc_effect.append(round(wc_temp[i] - air_temp[i], 1))

#создаём файл и записываем в него
with open(f'{n}.WindChillReport.txt', 'w', encoding='utf-8') as file2:
    file2.write('Time     WC temp     WC Effect\n')
    file2.write('-' * 30 + '\n')

    #записываем отформатированные строки
    for i in range(len(time)):
        file2.write(time[i] + f' {wc_temp[i]: >7} {wc_effect[i]: >13}\n')

    #записываем финальную строчку файла, используя среднее арифметическое всех температур
    file2.write('-' * 30 + '\n\n')
    file2.write(f'The average adjusted temperature, based on {len(time)} observations, was {round(average(wc_temp), 1)}\n')