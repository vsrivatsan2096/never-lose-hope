import re
import csv
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# impoting the dataset
data = pd.read_csv("reddit_jokes.csv")
X = data.iloc[:, 0:-1].values
y = data.iloc[:, -1].values

corpus = []
stem = PorterStemmer()
set_stopwords = set(stopwords.words("english"))
for i in X:
    joke = re.sub(r"[^A-Za-z]", " ", i[0])
    joke = joke.lower().split()
    joke = [stem.stem(word) for word in joke if not word in set_stopwords]
    corpus.append(" ".join(joke))

with open("cleaned_reddit_jokes.csv", "w") as file:
    csv_writter = csv.writer(file, quoting=csv.QUOTE_ALL)
    for joke, score in zip(corpus, y):
        csv_writter.writerow([joke, score])


data = pd.read_csv("stupid_jokes.csv")
X = data.iloc[:, 0:-1].values
y = data.iloc[:, -1].values

corpus = []
for i in X:
    joke = re.sub(r"[^A-Za-z]", " ", i[0])
    joke = joke.lower().split()
    joke = [stem.stem(word) for word in joke if not word in set_stopwords]
    corpus.append(" ".join(joke))

with open("cleaned_stupid_jokes.csv", "w") as file:
    csv_writter = csv.writer(file, quoting=csv.QUOTE_ALL)
    for joke, score in zip(corpus, y):
        csv_writter.writerow([joke, score])