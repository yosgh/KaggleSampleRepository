from gensim.models import word2vec
import sys
args = sys.argv

model = word2vec.Word2Vec.load("/Users/yoshidamasatoshi/pyenv/wikiextractor-master/wiki.model")

while 1:
    print("\nA - B + C = ?")

    print("\nA を入力してください")
    while True:
        print("> ", end="")
        strA = input()
        #model上に単語が存在した場合にbreakする
        if strA != "":
            if strA in model.wv:
                break
            print('{0} はみつかりません'.format(strA))

    print("\nB を入力してください")
    while True:
        print("> ", end="")
        strB = input()
        #model上に単語が存在した場合にbreakする
        if strB != "":
            if strB in model.wv:
                break
            print('{0} はみつかりません'.format(strB))

    print("\nC を入力してください")
    while True:
        print("> ", end="")
        strC = input()
        #model上に単語が存在した場合にbreakする
        if strC != "":
            if strC in model.wv:
                break
            print('{0} はみつかりません'.format(strC))

    print("\n---------------")
    print("A - B + C")
    print("---------------")
    results = model.wv.most_similar(positive=[strA, strC], negative=[strB], topn = 5)
    for i, result in enumerate(results):
        print('{0}:{1}'.format(i + 1, result[0]))
    print("---------------")
