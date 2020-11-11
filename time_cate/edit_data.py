import csv
from datetime import datetime

"""
    "monday": {
        "morning": 0,
        "afternoon": 0,
        "night": 0
    },
    days goes monday to sundays and time of day goes morning/afternoon/night
"""

days = {
    0: {
        0: 0,
        1: 0,
        2: 0
    },
    1: {
        0: 0,
        1: 0,
        2: 0
    },
    2: {
        0: 0,
        1: 0,
        2: 0
    },
    3: {
        0: 0,
        1: 0,
        2: 0
    },
    4: {
        0: 0,
        1: 0,
        2: 0
    },
    5: {
        0: 0,
        1: 0,
        2: 0
    },
    6: {
        0: 0,
        1: 0,
        2: 0
    },
}


def get_day_time_slot(datetime):
    weekday = datetime.weekday()
    if datetime.hour < 8:
        time_of_day = 0
    elif datetime.hour < 16:
        time_of_day = 1
    elif datetime.hour < 24:
        time_of_day = 2
    else:
        time_of_day = 0

    return {"weekday": weekday, "time_of_day": time_of_day}


with open('../scrobbles-kjevo-1604503776.csv', encoding='utf8') as file:
    csv_reader = csv.reader(file, delimiter=',')

    # 05 Jun 2016, 02:09
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            datetime_obj = datetime.strptime(row[1], "%d %b %Y, %H:%M")

            time_slot = get_day_time_slot(datetime_obj)

            days[time_slot["weekday"]][time_slot["time_of_day"]] += 1
        else:
            line_count += 1

    print(days)


with open('edited-data-time-cat.csv', mode='w', encoding='utf8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    file_writer.writerow([days[0][0], days[1][0], days[2][0], days[3][0], days[4][0], days[5][0], days[6][0]])
    file_writer.writerow([days[0][1], days[1][1], days[2][1], days[3][1], days[4][1], days[5][1], days[6][1]])
    file_writer.writerow([days[0][2], days[1][2], days[2][2], days[3][2], days[4][2], days[5][2], days[6][2]])
