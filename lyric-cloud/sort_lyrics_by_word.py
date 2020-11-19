import os

from lyricsgenius import Genius
import nltk


def get_clean_words(lyric):
    def _isnum(w):
        try:
            int(w)
            return True
        except ValueError:
            return False

    words = lyric.split(" ")
    words = [w.replace('\n', ' ') for w in words]

    temp_words_list = list()
    for word in words:
        if " " in word:
            temp_words = word.split(" ")
            for temp_word in temp_words:
                temp_words_list.append(temp_word)

    words = temp_words_list

    # Set words to lowercase and remove them if they are stop words
    words = [w.lower() for w in words if w.lower() not in stopwords]

    # Remove punctuation
    words = [w.replace('(', '') for w in words]
    words = [w.replace(')', '') for w in words]
    words = [w.replace('?', '') for w in words]
    words = [w.replace(',', '') for w in words]
    words = [w.replace('.', '') for w in words]
    words = [w.replace('[', '') for w in words]
    words = [w.replace(']', '') for w in words]
    words = [w.replace('"', '') for w in words]
    words = [w.replace('!', '') for w in words]
    words = [w.replace('\'', '') for w in words]
    words = [w.replace('\'s', '') for w in words]

    # Remove numbers
    words = [w for w in words if not _isnum(w)]

    # Only keep words with more than two characters
    words = [w for w in words if len(w) > 2]

    return words


def force_unique_list(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


genius = Genius("h11DjsYbJAHm4qVWyL8w34eeaTmdBugoHepwzuoTsWr-wBn5Zy8C0v9YYLwKFr1n-enbg8NfCP3TmaM-m8O6lQ",
                skip_non_songs=True, remove_section_headers=True)
stopwords = nltk.corpus.stopwords.words("english")

counter = 0
saved_words_dict = dict()
for file in os.listdir("C:\\Users\\kjell\\PycharmProjects\\MusicVis\\lyric-cloud\\editedlyrics"):
    if file.endswith(".txt"):
        with open("editedlyrics\\" + file, 'r', encoding='utf8') as text_file:
            words = get_clean_words(text_file.read())
            words = force_unique_list(words)

            for key in words:
                if key not in saved_words_dict.keys():
                    saved_words_dict[key] = 1
                else:
                    saved_words_dict[key] += 1

            counter += 1
            print(counter)


temp_dict = dict()
saved_words_dict_sorted_keys = sorted(saved_words_dict, key=saved_words_dict.get, reverse=True)
for word in saved_words_dict_sorted_keys:
    temp_dict[word] = saved_words_dict[word]

saved_words_dict = temp_dict
print(saved_words_dict)

counter = 0
out_file = open("data-lyrics.csv", "w", encoding='utf8')
for key in saved_words_dict.keys():
    out_file.write(f"{key},{saved_words_dict[key]}\n")
    counter += 1
    print(counter)
