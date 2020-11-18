import csv
import os
import re
import time

import lyricsgenius as lg
import nltk as nltk

genius = lg.Genius("h11DjsYbJAHm4qVWyL8w34eeaTmdBugoHepwzuoTsWr-wBn5Zy8C0v9YYLwKFr1n-enbg8NfCP3TmaM-m8O6lQ",
                   skip_non_songs=True, remove_section_headers=True)

saved_words_dict = dict()
with open('artist_song.txt', encoding='utf8') as file:
    csv_reader = csv.reader(file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count > 0:  # Limit with another and like 10 > line_count
            artist = row[0]
            title = row[1]

            string = artist + " " + title;
            string = re.sub('[^0-9a-zA-Z]+', '', string)
            if string in open('artist_song_done.txt', 'r').read():
                print("Skipping " + string)
            else:
                song = genius.search_song(title, artist, get_full_info=False)
                if song is not None:
                    lyric_txt = open('lyrics\\' + string + '.txt', encoding='utf8', mode='w')
                    lyric_txt.write(song.lyrics)

                open('artist_song_done.txt', 'a+').write(string + '\n')
                print(9050 - line_count)
                time.sleep(0.5)

        line_count += 1
