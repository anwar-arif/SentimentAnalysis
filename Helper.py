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

