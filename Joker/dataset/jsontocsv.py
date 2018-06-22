import csv
import json

reddit_jokes = json.load(open("reddit_jokes.json"))
with open("reddit_jokes.csv", "w") as file:
    csv_writter = csv.writer(file, quoting=csv.QUOTE_ALL)
    for each in reddit_jokes:
        if each.get("score"):
            csv_writter.writerow([each.get("title", "") + " " + each["body"], each["score"]])

stupid_jokes = json.load(open("stupidstuff.json"))
with open("stupid_jokes.csv", "w") as file:
    csv_writter = csv.writer(file, quoting=csv.QUOTE_ALL)
    for each in stupid_jokes:
        if each.get("rating"):
            csv_writter.writerow([each.get("category", "") + " " + each["body"], each["rating"]])

