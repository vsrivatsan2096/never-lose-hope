import json
import re

with open("jokes.txt", "w") as jokes:
    reddit_jokes = json.load(open("reddit_jokes.json"))
    for each in reddit_jokes:
        jokes.write(each.get("title", "") + " " + each["body"])

    stupid_jokes = json.load(open("stupidstuff.json"))
    for each in stupid_jokes:
        jokes.write(each["body"])

    wocka_jokes = json.load(open("wocka.json"))
    for each in wocka_jokes:
        jokes.write(each.get("title", "") + " " + each["body"])

with open("cleaned_jokes.txt", "w") as jp:
    for eachline in open("jokes.txt", "r"):
        jp.write(re.sub(r"[\n]", " ", eachline))
