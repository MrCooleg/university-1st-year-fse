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
