import sys
import re
import pandas
import MeCab

csv_name = sys.argv[1]
wakati_name = csv_name + ".wakati"

csv_header = ('created_at', 'service_name', 'source_id', 'source_url',
              'user_id', 'user_name', 'text', 'shared_by', 'csv_write_at')
data_frame = pandas.read_csv(csv_name, encoding="utf-8", names=csv_header)

parts = ["名詞", "動詞", "形容詞", "副詞", "未知語"]

# URL, screen_name, 記号
regex = r"https?://[a-zA-Z0-9\.\-_/]+|@[a-zA-Z0-9_]+|[^ぁ-んァ-ンーa-zA-Z0-9一-龠０-９]"

tagger = MeCab.Tagger("-Ochasen")
# https://qiita.com/kasajei/items/0805b433f363f1dba785 と同じ症状になったので一回parseをする
tagger.parse("")

writer = open(wakati_name, "w")

for text in data_frame["text"]:
    newtext = re.sub(regex, " ", text)
    node = tagger.parseToNode(newtext)

    while node:
        feature = node.feature.split(",")
        if feature[0] in parts:
            if feature[6] == "*":  # 未知語はそのまま出したい
                writer.write(node.surface + " ")
            else:
                writer.write(feature[6] + " ")
        node = node.next
    writer.write("\n")

writer.close()

