import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

# читаем файл с погодными данными
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = dt.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print('Missing data for ', current_date)
        else:
            # выводим в список даты
            dates.append(current_date)
            # выводим в список максимальные значения температур
            highs.append(high)
            # выводим в список минимальные значения температур
            lows.append(low)

    # print(highs)

# пронумерованный список
# for index, column_header in enumerate(header_row):
#     print(index + 1, column_header)

# нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10,6))

# прорисовка двух линий данных по температурам
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# заполнение пространства на диаграмме между данными
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# форматирование диаграммы
plt.title('Daily high and low temperatures, 2014\nDeath Valley, CA', 
            fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()