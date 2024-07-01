import calendar

# print(calendar.calendar(theyear=2024))
# print(calendar.month(2024, 6))
# dia_semana, data = calendar.monthrange(2024, 6)
# print(list(calendar.day_name)[dia_semana])

# print(list(calendar.day_name)[calendar.weekday(2024, 6, 30)])

for week in calendar.monthcalendar(2024, 6):
    for day in week:
        if day == 0:
            continue
        print(day)