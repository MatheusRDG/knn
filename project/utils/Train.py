import pickle
from project.utils.TextExtractor import TextExtractor
class Train:
    def __init__(self, data = [], allWords = {}):
        self.data = data
        self.allWords = allWords

    def saveData(self):
        with open('train.txt', 'wb') as fp:
            pickle.dump([self.allWords, self.data], fp)

    def loadData(self):
        with open('train.txt', 'rb') as fp:
            self.allWords, self.data = pickle.load(fp)

    def trainDataSet(self, negativeText = False, positiveText = False):

        if negativeText:
            textExtractor = TextExtractor(negativeText,positiveText)
        else:
            textExtractor = TextExtractor()

        negText, posText = textExtractor.extractFromDataSet()

        #print(negText)
        self.allWords = textExtractor.dic

        trainFrequencyList = []
        listAllWords = list(self.allWords.keys())
        lenAllWords = len(listAllWords)

        for i in negText:
            listTemp = [0] * lenAllWords
            for j in i:
                try:
                    self.allWords[j]
                    listTemp[listAllWords.index(j)] = i.count(j)
                except:
                    pass
            trainFrequencyList.append((listTemp,'N'))

        for i in negText:
            listTemp = [0] * lenAllWords
            for j in i:
                try:
                    self.allWords[j]
                    listTemp[listAllWords.index(j)] = i.count(j)
                except:
                    pass
            trainFrequencyList.append((listTemp,'P'))

        self.data = trainFrequencyList
