import sys
import os
import json
import random

sentence = []

chain = json.load(open(sys.argv[1], "r"))

first_word = random.choice(list(chain.keys()))
sentence.append(first_word)

second_word = random.choice(list(chain[first_word].keys()))
if first_word.encode("utf-8").isalpha() and second_word.encode("utf-8").isalpha():
    sentence.append(" ")
sentence.append(second_word)

while True:
    next_word = random.choice(list(chain[first_word][second_word].keys()))
    if next_word == "":
        break
    if second_word.encode("utf-8").isalpha() and next_word.encode("utf-8").isalpha():
        sentence.append(" ")

    sentence.append(next_word)
    first_word, second_word = second_word, next_word

print("".join(sentence))
