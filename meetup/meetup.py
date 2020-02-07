from datetime import date

import calendar


class MeetupDayException(Exception):
    def __init__(self, error):
        self.error = error


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:

    day_dict = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }

    day_dict = dict(zip(list(calendar.day_name), range(7)))

    week_dict = {
        "1st": 0,
        "2nd": 1,
        "3rd": 2,
        "4th": 3,
        "5th": 4,
        "last": -1,
        "teenth": (13, 16, 19),
    }

    meet = calendar.Calendar(firstweekday=6)

    meet_list = [
        i
        for i in meet.itermonthdays4(year, month)
        if i[3] == day_dict[day_of_week] and i[1] == month
    ]

    if week == "teenth":
        meet_date = [x for x in meet_list if x[2] in week_dict[week]][0]
    else:
        try:
            meet_date = meet_list[week_dict[week]]
        except IndexError as e:
            raise MeetupDayException(e)

    return date(meet_date[0], meet_date[1], meet_date[2])
