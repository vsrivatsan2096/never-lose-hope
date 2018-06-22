from sklearn.preprocessing import MinMaxScaler
from pandas import read_csv
import csv

data = read_csv("reddit_jokes.csv")
X = data.iloc[:, 0].values
y = data.iloc[:, 1:].values

sc = MinMaxScaler((1, 5))
y = sc.fit_transform(y)

with open("classed_cleaned_reddit_jokes.csv", "w") as file:
    csv_writter = csv.writer(file, quoting=csv.QUOTE_ALL)
    for joke, score in zip(X, y):
        csv_writter.writerow([joke, int(score[0])])
