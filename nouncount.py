import re
import sys
import MeCab
import pandas as pd
from collections import Counter

args = sys.argv
file_name = "data.csv"
if len(args) >= 2:
    file_name = args[1]
top = 10
if len(args) >= 3:
    top = int(args[2])

csv_header = ('created_at', 'service_name', 'source_id', 'source_url',
              'user_id', 'user_name', 'text', 'shared_by', 'csv_write_at')
data_frame = pd.read_csv(file_name, encoding="utf-8", names=csv_header)

mcb = MeCab.Tagger("-Ochasen")
# https://qiita.com/kasajei/items/0805b433f363f1dba785 と同じ症状になったので
# 一回先にparseをする
mcb.parse("")

counter = Counter()

repl = ""
regex_url = r"https?://[a-zA-Z0-9\.\-_/]+"
regex_twitter_screen_name = r"@[a-zA-Z0-9_]+"

for text in data_frame["text"]:
    text = re.sub(regex_url, repl, text)
    text = re.sub(regex_twitter_screen_name, repl, text)

    node = mcb.parseToNode(text)
    while node:
        if node.feature.split(",")[0] == "名詞" \
        and node.feature.split(",")[1] == "一般":
            print(node.surface + '\t' + node.feature)
            counter[node.surface] += 1
        node = node.next
    print("----------------------------------------------------")

for word, count in counter.most_common(top):
    print(word, count)