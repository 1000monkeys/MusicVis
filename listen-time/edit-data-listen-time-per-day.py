import csv
from datetime import datetime
import pandas as pd

string_begin = '2015-06-17'
string_end = '2020-11-04'

data = {}
with open('../scrobbles-kjevo-1604503776.csv', encoding='utf8') as file:
    csv_reader = csv.reader(file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            time = row[1][0:11]
            time = datetime.strptime(time, '%d %b %Y')

            if time.date() in data.keys():
                data[time.date()]["plays"] += 1
            else:
                data[time.date()] = {'date': time.date().strftime("%Y/%m/%d"), 'plays': 1}

        line_count += 1

    with open('data-edited-listen-time-per-day.csv', mode='w', newline='') as data_edited:
        state_writer = csv.writer(data_edited, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        state_writer.writerow(["date", "plays"])
        for key in data.keys().__reversed__():
            state_writer.writerow([data[key]["date"], data[key]["plays"]])
