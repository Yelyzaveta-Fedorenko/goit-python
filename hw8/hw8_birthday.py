from datetime import datetime, timedelta

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

    users = [
        {"name": "Fedir", "birthday": datetime.fromisoformat("1998-07-16 10:10:10")},
        {"name": "Maksym", "birthday": datetime.fromisoformat("2021-03-18 10:10:10")},
        {"name": "Leonid", "birthday": datetime.fromisoformat("2001-05-19 10:10:10")},
        {"name": "Kostiantyn", "birthday": datetime.fromisoformat("1990-12-17 10:10:10")},
        {"name": "Serhii", "birthday": datetime.fromisoformat("1991-10-27 10:10:10")},
        {"name": "Valentyn", "birthday": datetime.fromisoformat("1970-04-20 10:10:10")},
        {"name": "Mykola", "birthday": datetime.fromisoformat("1989-01-11 10:10:10")},
        {"name": "Mykhailo", "birthday": datetime.fromisoformat("1983-12-12 10:10:10")},
        {"name": "Ivan", "birthday": datetime.fromisoformat("1972-01-21 10:10:10")}
    ]
    

get_birthdays_per_week(users)