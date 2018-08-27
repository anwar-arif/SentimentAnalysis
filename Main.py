import Helper
import Word2Vec
# import CNN

positive, negative = Helper.Partition_Pos_Neg_Data()
sentences = Helper.Get_Sentences(positive, negative)

Word2Vec.Do_Word2Vec(sentences)
# CNN.Do_CNN(positive, negative)


