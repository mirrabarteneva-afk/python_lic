from datetime import datetime, timedelta


months = (
    "Лев", "Колдунья", "Фавн", "Бобр", "Кентавр",
    "Орланд", "Древо", "Фонарь", "Дуб"
)
week_days_narnia = (
    "Понд", "Вторнд", "Тринд", "Четв",
    "Пятн", "Шестн", "Седьмидень", "Восьмидень"
)
presents = (
    "День Творения", "День Пробуждения", "День Даров",
    "День Пророчества", "День Возвращения"
)
week_days = (
    "Понедельник", "Вторник", "Среда", "Четверг",
    "Пятница", "Суббота", "Воскресенье"
)

data_world = datetime.strptime(input(), "%d.%m.%Y")
data_narnia = input()

if data_narnia in presents:
    ind = presents.index(data_narnia)
    day_now = data_world + timedelta(days= 40 * 9 + ind)
    day_now_week = week_days[datetime.weekday(day_now)]
    day_now = day_now.strftime('%d.%m.%Y')
    print(ind + 1)
    print(f'{day_now_week}, {day_now}')
    
else:
    data_narnia = data_narnia.split()
    day_now = data_world + timedelta(days= 40 * months.index(data_narnia[1]) + int(data_narnia[0]) - 1)
    day_now_week = week_days[datetime.weekday(day_now)]
    week_days_narnia = week_days_narnia * int(data_narnia[0])
    day_narnia_week = week_days_narnia[int(data_narnia[0]) - 1]
    day_now = day_now.strftime('%d.%m.%Y')
    print(day_narnia_week)
    print(f'{day_now_week}, {day_now}')


