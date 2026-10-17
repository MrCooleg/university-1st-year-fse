#просим ввести строку данных
while True:
    packets = input()

    #сразу ищем длину строки
    total = len(packets)

    #если строка не прошла проверки, просим ввести заново
    if total < 5:
        print('Строка слишком короткая')
    else:
        #для всех символов строки проверка на принадлежность строке разрешённых символов
        if not all(char in '01' for char in packets):
            print("Неверный ввод. Используйте только символы '0' и '1'!")
        else:
            break

#получаем количество всех нулей
lost_total = packets.count('0')

#делим строку на список последовательностей нулей через разделение по символу '1'
lost_sequences = packets.split('1')

#объявляем список длин последовательностей
sequence_lengths = []

#для каждой последовательности ищем её длину и записываем в sequence_lengths
for i in range(len(lost_sequences)):
    sequence_lengths.append(len(lost_sequences[i]))

#ищем наибольший элемент списка длин последовательностей
lost_max_len = max(sequence_lengths)

#ищем процент потерь
lost_percentage = lost_total * 100 / total

#проверяем качество сети
if 0 <= lost_percentage <= 1:
    quality = 'отличное'
elif 1 < lost_percentage <= 5:
    quality = 'хорошее'
elif 5 < lost_percentage <= 10:
    quality = 'удовлетворительное'
elif 10 < lost_percentage <= 20:
    quality = 'плохое'
else:
    quality = 'критическое состояние сети'

#выводим результат
print('Общее количество пакетов:', total)
print('Количество потерянных пакетов:', lost_total)
print('Длина самой длинной последовательности потерянных пакетов:', lost_max_len)
print(f'Процент потерь: {lost_percentage:.1f}%')
print('Качество связи:', quality)