import csv

from wordcloud import WordCloud, STOPWORDS


dataset = dict()
with open('data-lyrics.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dataset[str(row[0])] = int(row[1])

print(dataset)

cloud = WordCloud(background_color="white", height=768, width=1024, max_words=200, stopwords=set())
cloud.fit_words(dataset)
cloud.to_file("wordCloud.png")