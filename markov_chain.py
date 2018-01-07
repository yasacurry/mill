import sys
import os
import json

chain = {}
window = 3

def read_wakati(file_name):
    wakati = open(file_name, "r")
    for line in wakati:
        make_chain(line)

def make_chain(line):
    words = line.split()
    if len(words) == 0:
        return
    if len(words) == 1:
        words.append("")

    for i, x in enumerate(words):
        if i > len(words) - window:
            break
        set_words(*words[i:i+window])

    set_words(words[-2], words[-1], "")

def set_words(word1, word2, word3):
    if word1 not in chain:
        chain[word1] = {}
    if word2 not in chain[word1]:
        chain[word1][word2] = {}
    if word3 not in chain[word1][word2]:
        chain[word1][word2][word3] = 0
    chain[word1][word2][word3] += 1

wakati_name = sys.argv[1]
markov_name = wakati_name + ".markov"
read_wakati(wakati_name)
json.dump(chain, open(markov_name, "w"))

