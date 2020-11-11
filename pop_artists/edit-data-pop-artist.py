import collections
import csv

artists = list()
plays = {}

with open('../scrobbles-kjevo-1604503776.csv', encoding='utf8') as file:
    csv_reader = csv.reader(file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            artist = row[2]
            song = row[6]

            if artist not in artists:
                artists.append(artist)

            if artist in plays:
                plays[artist] += 1
            else:
                plays[artist] = 1

        line_count += 1

print(len(artists))
print(len(plays))


with open('edited-data-pop-artist.csv', mode='w', encoding='utf8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    file_writer.writerow(['artist', 'amount_of_plays'])
    plays = collections.Counter(plays)

    for key, value in plays.most_common(25):
        file_writer.writerow([key, value])
