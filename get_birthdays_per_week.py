from datetime import datetime, timedelta

# Словник створений для прикладу
users = [{'name': 'Aleks', 'birthday': datetime(year=1999, month=5, day=14)},
         {'name': 'Orest', 'birthday': datetime(year=2001, month=5, day=14)},
         {'name': 'Maks', 'birthday': datetime(year=2002, month=5, day=19)},
         {'name': 'Diana', 'birthday': datetime(year=1997, month=5, day=12)},
         {'name': 'Andriy', 'birthday': datetime(year=2002, month=5, day=17)},
         {'name': 'Oleg', 'birthday': datetime(year=2001, month=6, day=15)}]

current_datetime = datetime.now()
one_weeks_interval = timedelta(weeks=1)
one_week_ago = current_datetime + one_weeks_interval  # отримуємо день через тиждень від сьогоднішнього


def get_birthdays_per_week(dictionary):
    birthdays = {}
    for user in dictionary:
        birthday = user.get('birthday')
        name = user.get('name')

        # отримуємо дату дня народження цього року
        this_year_birthday = datetime(year=datetime.today().year, month=birthday.month, day=birthday.day)

        # день тижня коли у співробітника день народження в цьому році
        day_of_week = this_year_birthday.strftime('%A')

        if current_datetime.strftime("%m-%d") <= this_year_birthday.strftime("%m-%d") < one_week_ago.strftime("%m-%d"):
            # якщо день народження в суботу або неділю - привітати треба в понеділок
            if day_of_week == 'Saturday':
                day_of_week = 'Monday'
            elif day_of_week == 'Sunday':
                day_of_week = 'Monday'

            # Натсупні рядки коду перевіряють, чи є ключ з назвою дня тижня day_of_week в словнику birthdays.
            # Якщо є, тоді до списку значень, що відповідають цьому ключу, додається ім'я людини name.
            # Якщо такого ключа немає, тоді створюється новий ключ з цією назвою дня тижня, і до списку значень,
            # що відповідають цьому ключу, додається ім'я людини name.

            if day_of_week in birthdays:
                birthdays[day_of_week].append(name)
            else:
                birthdays[day_of_week] = [name]

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")


if __name__ == '__main__':
    get_birthdays_per_week(users)
