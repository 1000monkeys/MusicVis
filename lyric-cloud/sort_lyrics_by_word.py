from lyricsgenius import Genius
import nltk

genius = Genius("h11DjsYbJAHm4qVWyL8w34eeaTmdBugoHepwzuoTsWr-wBn5Zy8C0v9YYLwKFr1n-enbg8NfCP3TmaM-m8O6lQ",
                skip_non_songs=True, remove_section_headers=True)

nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words("english")

def get_clean_words(lyric):
    def _isnum(w):
        try:
            int(w)
            return True
        except ValueError:
            return False

    words = lyric.split(" ")

    # Set words to lowercase and remove them if they are stop words
    words = [w.lower() for w in words if w.lower() not in stopwords]

    # Remove punctuation
    words = [w.replace('(', '') for w in words]
    words = [w.replace(')', '') for w in words]
    words = [w.replace('?', '') for w in words]
    words = [w.replace(',', '') for w in words]
    words = [w.replace('.', '') for w in words]
    words = [w.replace('"', '') for w in words]
    words = [w.replace('!', '') for w in words]
    words = [w.replace('\'s', '') for w in words]
    words = [w.replace('\n', ' ') for w in words]

    temp_words = list()
    for word in words:
        if " " in word:
            temp_temp_words = word.split(" ")
            for temp_temp_words_temp in temp_temp_words:
                temp_words.append(temp_temp_words_temp)

    words = temp_words

    # Remove numbers
    words = [w for w in words if not _isnum(w)]

    # Only keep words with more than one character
    words = [w for w in words if len(w) > 1]

    return words


out_file = open("data-lyrics.csv", "w", encoding='utf8')
for key in saved_words_dict:
    out_file.write(f"{key},{saved_words_dict[key]}\n")


words = get_clean_words(song.lyrics)

for word in words:
    if word not in saved_words_dict.keys():
        saved_words_dict[word] = 1
    else:
        saved_words_dict[word] += 1
