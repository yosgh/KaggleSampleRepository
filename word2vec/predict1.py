from gensim.models import word2vec
import sys
args = sys.argv

model = word2vec.Word2Vec.load("/Users/yoshidamasatoshi/pyenv/wikiextractor-master/wiki.model")

while 1:
    print("単語を入力してください") #出力：文字列
    str = input() # 文字列を取得し、strに値を入れる


    print("similarity TOP10") #出力：文字列
    print("================") #出力：文字列
    results = model.wv.most_similar(positive=[str])
    for result in results:
        print(result)

    print("") #改行