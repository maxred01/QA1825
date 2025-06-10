banner_name = list(['Ваня', 'Дима', 'Витя'])
name_user = input('Введите свое имя: ').lower()
if name_user in banner_name:
    print('Доступ запрещён: вы находитесь в списке запрещённых.')

sos_siutuacia = input("Экстренная ситуация? (да/нет): ").lower()
if sos_siutuacia == 'да':
    print('доступ в зону: доступ всем')

role = input('Введите свою роль: (Сотрудник/Контрагент/Гость): ') .lower()
if role == 'сотрудник':
    print('доступ в зону:  всегда')
elif role == 'контрагент':
    day_week = input('Введите день недели: ') .lower()
    if day_week in ["суббота", "воскресенье"]:
        print("Доступ запрещён: для контрагентов доступ только в будние дни.")
    else:
        time = input("Введите текущее время (чч:мм): ").strip()
        if time:
            hours, minutes = map(int, time.split(':'))
        else:
            print("Неверный формат времени.")
            exit()
            # Преобразуем время в минуты от начала суток для удобства сравнения
        time_minutes = hours * 60 + minutes
        start_minutes = 9 * 60  # 09:00 → 540 минут
        end_minutes = 18 * 60  # 18:00 → 1080 минут

        if start_minutes <= time_minutes <= end_minutes:
            print("Доступ разрешён.")
        else:
            print("Доступ запрещён: контрагентам доступ только с 09:00 до 18:00 в будние дни.")
elif role == 'гость':
    escort = input("Сопровождает ли вас сопровождающий? (да/нет): ")
    if escort == 'да':
         print("Доступ разрешен")
    else:
        print('Доступ запрещён')
else:
    print("Неверная роль пользователя.")
