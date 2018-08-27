from gensim.models import Word2Vec as wv

def Do_Word2Vec(sentences) :
    modelPath = "G:\semester\semester 4-2\Thesis\Codes\SentimentAnalysis\Main\word2vec.txt"

    # sentences = [['first', 'sentence'], ['second', 'sentence']]
    model = wv(sentences, size=5, min_count=1)
    model.save(modelPath)

    print(model.similarity('মেসি', 'নেইমার'))
    print(model['নেইমার'])


