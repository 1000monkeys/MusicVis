import csv

with open('../scrobbles-kjevo-1604503776.csv', encoding='utf8') as file:
    csv_reader = csv.reader(file, delimiter=',')

    file_artist_song = open("artist_song.txt", "w", encoding='utf8')

    present_check_list = list()
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            artist = row[2]
            title = row[6]

            id_string = f"{artist} - { title}"
            if id_string not in present_check_list:
                file.write(f"{artist},{title}\n")
                present_check_list.append(id_string)

        line_count += 1