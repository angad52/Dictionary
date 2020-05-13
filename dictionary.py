#!/usr/bin/env python

from difflib import get_close_matches
import json

data = json.load(open("data.json"))


def find(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s?" % get_close_matches(word, data.keys())[0])
        decide = input("y or n : ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return "Wrong Input."
        else:
            return "Wrong Input Key. Enter y or n only. "
    else:
        return "Wrong Input."


x = 'y'
while x == 'y':
    word = input("Enter the word: ")
    output = find(word)
    if type(output) == list:
        for i in output:
            print(i)
    else:
        print(output)

    x = input("Another Word y or n: ")
