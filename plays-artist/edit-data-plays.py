import csv

songs = list()
artists = list()
plays = {}
amount_of_songs = {}

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

            if song not in songs:
                songs.append(song)

                if artist in amount_of_songs.keys():
                    amount_of_songs[artist] += 1
                else:
                    amount_of_songs[artist] = 1

        line_count += 1


print(len(artists))
print(len(plays))
print(len(amount_of_songs))


with open('edited-data-plays.csv', mode='w', encoding='utf8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    file_writer.writerow(['artist', 'amount_of_songs', 'amount_of_plays'])
    for artist in artists:
        if artist in amount_of_songs.keys() and artist in plays.keys():
            file_writer.writerow([str(artist), amount_of_songs[str(artist)], plays[str(artist)]])
