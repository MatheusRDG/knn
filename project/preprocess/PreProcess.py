import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

def prePreprocess(string):

    #Remove Characters
    result = list(map(lambda i: re.sub('[^A-Za-z0]+', ' ', i), [string]))

    #Token
    result = list(map(lambda i: word_tokenize(i), result))

    # StopWords
    result = [[i for i in sentences if i not in stopwords.words('english')] for sentences in result]

    #Lemm
    lemmatizer = WordNetLemmatizer()
    result = list(map(lambda i: list(map(lambda j: lemmatizer.lemmatize(j),i)),result))

    #Stemm
    #stemmer = SnowballStemmer('english')
    #result = list(map(lambda i: list(map(lambda j: stemmer.stem(j), i)), result))

    return result[0]