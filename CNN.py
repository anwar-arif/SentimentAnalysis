from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM, Flatten, Convolution1D, Dropout
from keras.layers import Embedding
from keras.preprocessing import sequence
from keras.callbacks import TensorBoard

import Helper


positive_docs = 3681
negative_docs = 4500
testing_docs = 2000
max_review_length = 311

def Do_CNN(positive, negative, model) :
    max_review_length = 310
    X_train, Y_train = Helper.Get_Data(0, positive, negative, model)
    X_test, Y_test = Helper.Get_Data(1, positive, negative, model)

    print(len(X_train), len(Y_train))
    print(len(X_test), len(Y_test))

    # for v in X_train[0] :
    #     print(v)