import sys
import re
import argparse
import pandas
import MeCab

parser = argparse.ArgumentParser()
parser.add_argument("csv", help="target file (github.com/yasacurry/harvest)")
parser.add_argument(
    "-s",
    "--surface",
    help="use MeCab-chasen type surface",
    action="store_true")
args = parser.parse_args()

csv_header = ('created_at', 'service_name', 'source_id', 'source_url',
              'user_id', 'user_name', 'text', 'shared_by', 'csv_write_at')
data_frame = pandas.read_csv(args.csv, encoding="utf-8", names=csv_header)

parts = ["名詞", "動詞", "形容詞", "副詞", "未知語"]

# URL, screen_name, 記号
regex = r"https?://[a-zA-Z0-9\.\-_/]+|@[a-zA-Z0-9_]+|[^ぁ-んァ-ンーa-zA-Z0-9一-龠０-９]"

tagger = MeCab.Tagger("-Ochasen")
# https://qiita.com/kasajei/items/0805b433f363f1dba785 と同じ症状になったので一回parseをする
tagger.parse("")

writer = open(args.csv + ".wakati", "w")

for text in data_frame["text"]:
    newtext = re.sub(regex, " ", text)
    node = tagger.parseToNode(newtext)

    while node:
        feature = node.feature.split(",")
        if args.surface:
            writer.write(node.surface + " ")
        else:
            if feature[0] in parts:
                if feature[6] == "*":  # 未知語はそのまま出したい
                    writer.write(node.surface + " ")
                else:
                    writer.write(feature[6] + " ")
        node = node.next
    writer.write("\n")

writer.close()
