'''
The function prints in console a list of colleagues to wish happy birthday in the next seven days.
If the birhtday is on Saturday or Sunday it will be shifted to Monday in the list.
'''



from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    list_of_birthday = defaultdict(list)
    today = datetime.today().date()
    tomorrow = today + timedelta(days=1)
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()  
        birthday_this_year = birthday.replace(year=tomorrow.year)
        if birthday_this_year < tomorrow:
            birthday_this_year = birthday_this_year.replace(year = (tomorrow.year + 1))
        delta_days = (birthday_this_year - tomorrow).days
        if delta_days < 7:
            day_of_week = birthday_this_year.weekday()
            if day_of_week == 0:
                list_of_birthday['Monday'].append(name)
            elif day_of_week == 1:
                list_of_birthday['Tusday'].append(name)
            elif day_of_week == 2:
                list_of_birthday['Wenesday'].append(name)
            elif day_of_week == 3:
                list_of_birthday['Thursday'].append(name)
            elif day_of_week == 4:
                list_of_birthday['Friday'].append(name)
            elif day_of_week == 5 and today.weekday() != 5 and today.weekday() != 6:
                list_of_birthday['Monday'].append(name)
            elif day_of_week == 6 and today.weekday() != 6:
                list_of_birthday['Monday'].append(name)
    print(list_of_birthday)