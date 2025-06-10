weather = input('Погода (холодно/тепло): ').lower()
time_day = input('Время (утро/день/вечер/ночь): ').lower()
people = input('Наличие людей дома (да/нет): ').lower()

if time_day == 'ночь':
    print('на улице: 18°C')
elif people == 'нет':
    print('на улице: 16°C')
elif people == 'да' and weather == 'холодно':
    print('на улице: 22°C')
elif people == 'да' and weather == 'тепло':
    print('на улице: 20°C')
else:
    print('Ошибка ввода данных!')