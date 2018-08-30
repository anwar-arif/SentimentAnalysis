from openpyxl import load_workbook

punctuation = "-'#.,"
line_ending = "?!৷।"

# seperates positive and negative data in two lists and returns lists
def Partition_Pos_Neg_Data() :
    total_row = 8181

    xlPath = "G:\semester\semester 4-2\Thesis\Dataset\SentimentAnalysis"
    xlPath += "\{}\{}\{}".format("aclImdb_v1", "dataset", "sa_tagged_dataset.xlsx")

    book = load_workbook(xlPath)
    sheet = book.active
    positive, negative = [], []

    for i in range(1, total_row + 1) :
        if sheet['A' + str(i)].value == "pos" :
            positive.append(sheet['B' + str(i)].value)
        else:
            negative.append(sheet['B' + str(i)].value)

    return positive, negative

def english(word) :
    for c in word :
        if c >= 'A' and c <= 'Z' :
            return True
        if c >= 'a' and c <= 'z' :
            return False
    return False

# returns a list of words for each sentences
def Get_Words(line) :
    result, temp, word = [], [], ""

    for c in line :
        if c == ' ' :
            if len(word) > 0 and not english(word) :
                temp.append(word)
            word = ""
        elif c in line_ending :
            if len(word) > 0 and not english(word) :
                temp.append(word)
            if len(temp) > 0 :
                cur = []
                for t in temp :
                    cur.append(t)
                result.append(cur)
            temp.clear()
            word = ""
        elif c in punctuation :
            if len(word) > 0 and not english(word):
                temp.append(word)
            word = ""
        else :
            word += c

    if len(temp) > 0 :
        cur = []
        for t in temp :
            cur.append(t)
        result.append(cur)

    return result

# Generates a list of lists that contains list of words for each sentences
def Get_Sentences(positive, negative) :
    cnt, word, result, sentences = 0, "", [], []

    for sen in positive :
        temp = Get_Words(sen)
        for t in temp :
            sentences.append(t)

    for sen in negative :
        temp = Get_Words(sen)
        for t in temp :
            sentences.append(t)

    return sentences

def Sentence2Word(line) :
    result, temp, word = [], [], ""

    for c in line :
        if c == ' ' :
            if len(word) > 0 and not english(word) :
                temp.append(word)
            word = ""
        elif c in line_ending :
            if len(word) > 0 and not english(word) :
                temp.append(word)
            if len(temp) > 0 :
                for t in temp :
                    result.append(t)
            word = ""
            temp.clear()
        elif c in punctuation :
            if len(word) > 0 and not english(word):
                temp.append(word)
            word = ""
        else :
            word += c

    if len(temp) > 0 :
        for t in temp :
            result.append(t)

    return result

positive_docs = 3681
negative_docs = 4500
testing_docs = 2000
max_review_length = 311
zeros = [0 for i in range(5)]

def Get_Data(mark, positive, negative, model) :
    pl, pr, nl, nr = 0, 0, 0, 0
    if mark == 0 :
        pl, pr, nl, nr = 0, testing_docs, 0, testing_docs
    if mark == 1 :
        pl, pr, nl, nr = testing_docs, len(positive), testing_docs, len(negative)

    cur, temp = [], []
    X, Y = [], []
    for i in range(pl, pr) :
        words = Sentence2Word(positive[i])
        temp.clear()
        for w in words :
            cur.clear()
            for val in model[w] :
                cur.append(val)
            # temp.append(cur)
            temp.append(model[w])
        padding = max_review_length - len(temp)
        for j in range(padding) :
            temp.append(zeros)
        X.append(temp)
        Y.append(1)
    for i in range(nl, nr) :
        words = Sentence2Word(negative[i])
        temp.clear()
        for w in words :
            cur.clear()
            for val in model[w] :
                cur.append(val)
            # temp.append(cur)
            temp.append(model[w])
        padding = max_review_length - len(temp)
        for j in range(padding) :
            temp.append(zeros)
        X.append(temp)
        Y.append(0)

    return X, Y