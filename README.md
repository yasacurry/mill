# mill
[harvest](https://github.com/yasacurry/harvest) で保存したファイルの分かち書き、word2vecで遊ぶセット、マルコフ連鎖で遊ぶセット、単語の出現回数カウント

## usage 
- word2vecで遊びたい  
`$ python wakati.py data.csv`  
`$ python model.py data.csv.wakati`  
`$ python -i interactive.py data.csv.wakati.model`

- マルコフ連鎖で遊びたい  
`$ python wakati.py -s data.csv`  
`$ python markov_chain.py data.csv.wakati`  
`$ python markov_sentence data.csv.wakati.markov`

- 名詞の出現回数を知りたい
`$ python nouncount.py data.csv 10`