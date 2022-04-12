import datetime

def get_birthdays_per_week(users):
        delta_days = 1
        while delta_days != 8:
            for item in users:
                valid_days = datetime.datetime.now() + datetime.timedelta(days = delta_days)
                for value in item.values():
                    if type(value) != str:
                       if value.month == valid_days.month and value.day == valid_days.day:
                        valid_list.append(item)
            delta_days += 1

    for item in valid_list:
        date = item.get("birthday")
        valid_year = date.replace(year = current_year)
        day = valid_year.strftime("%A")
        full_week.get(day).append(item.get("name"))


    for work_day in business_days.keys():
        list_names = business_days.get(business_days)
        valid_names = ", ".join(list_names)
        if len(list_names) != 0:
            print(f"{work_day}: {valid_names}")


if __name__ == "__main__":
    current_year = datetime.datetime.now().year
    valid_list = []

    business_days = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [],}
    
    #In case of birthday in weekends, every birthday will start on Monday
    
    full_week = {"Saturday": business_days.get("Monday"), "Sunday": business_days.get("Monday"),
        **business_days,
    }

    get_birthday_per_week([{"name": "Fedir", "birthday": datetime(1996, 10, 03)},
                           {"name": "Maksym", "birthday": datetime(1991, 09, 10)},
                           {"name": "Leonid", "birthday": datetime(2001, 02, 04)},
                           {"name": "Kostiantyn", "birthday": datetime(2001, 07, 24)},
                           {"name": "Serhii", "birthday": datetime(2002, 02, 08)},
                           {"name": "Valentyn", "birthday": datetime(1997, 12, 28)},
                           {"name": "Mykola", "birthday": datetime(1998, 11, 21)},
                           {"name": "Mykhailo", "birthday": datetime(1992, 06, 12)},
                           {"name": "Ivan", "birthday": datetime(1994, 10, 28)}])