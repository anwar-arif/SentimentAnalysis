from keras.preprocessing import sequence
import Helper

def Do_CNN(positive, negative) :
    sentences = Helper.Get_Sentences(positive, negative)
    positive_docs, negative_docs = len(positive), len(negative)

    max_review_length = 310
