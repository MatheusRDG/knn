import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk import pos_tag
from nltk.corpus import stopwords

def prePreprocess(string):

    #Sentence Split
    #result = sent_tokenize(string)

    #Remove Characters
    result = list(map(lambda i: re.sub('[^A-Za-z0]+', ' ', i), [string]))

    #Token
    result = list(map(lambda i: word_tokenize(i), result))

    # StopWords
    #print(result)
    result = [[i for i in sentences if i not in stopwords.words('english')] for sentences in result]
    #print(result)

    #Lemm
    lemmatizer = WordNetLemmatizer()
    result = list(map(lambda i: list(map(lambda j: lemmatizer.lemmatize(j),i)),result))

    #Stemm
    stemmer = SnowballStemmer('english')
    result = list(map(lambda i: list(map(lambda j: stemmer.stem(j), i)), result))

    ##Pos Tagging
    #result = list(map(lambda i: pos_tag(i), result))

    #result2 = []
    #for i in result:
    #    for j in i:
    #        if j[1] == 'JJ' or j[1] == 'VB':
    #            result2.append(j)

    return result[0]

#print(prePreprocess('my name is matheus. i am from usa and im small'))
