import Helper
import Word2Vec
import CNN

positive, negative = Helper.Partition_Pos_Neg_Data()
sentences = Helper.Get_Sentences(positive, negative)

model = Word2Vec.Do_Word2Vec(sentences)

# print(model.similarity('মেসি', 'নেইমার'))
CNN.Do_CNN(positive, negative, model)

# words = Helper.Sentence2Word(positive[0])
# for w in words :
#     print(w)