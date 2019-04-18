import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk import pos_tag

def preProcess(string):

    #Sentence Split
    result = sent_tokenize(string)

    #Remove Characters
    result = list(map(lambda i: re.sub('[^A-Za-z0]+', ' ', i), result))

    #Token
    result = list(map(lambda i: word_tokenize(i), result))

    #Lemm
    lemmatizer = WordNetLemmatizer()
    result = list(map(lambda i: list(map(lambda j: lemmatizer.lemmatize(j),i)),result))

    #Stemm
    stemmer = SnowballStemmer('english')
    result = list(map(lambda i: list(map(lambda j: stemmer.stem(j), i)), result))

    #Pos Tagging
    result = list(map(lambda i: pos_tag(i), result))

    return result

#print(prePreprocess('my name is matheus. i am from usa'))