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

    def trainWithSpecifiedSet(self, positiveTrain, negativeTrain):

        self.allWords = {word: '' for word in list(set([j for i in positiveTrain for j in i] + [j for i in negativeTrain for j in i]))}

        trainFrequencyList = []
        listAllWords = list(self.allWords.keys())
        lenAllWords = len(listAllWords)

        tempDict = {i[1]: i[0] for i in list(enumerate(listAllWords))}

        for i in negativeTrain:
            listTemp = [0] * lenAllWords
            for j in i:
                listTemp[tempDict[j]] += 1
            trainFrequencyList.append((listTemp, 'N'))

        for i in positiveTrain:
            listTemp = [0] * lenAllWords
            for j in i:
                listTemp[tempDict[j]] += 1
            trainFrequencyList.append((listTemp, 'P'))

        self.data = trainFrequencyList

    def trainDataSet(self, negativeText = False, positiveText = False):

        if negativeText:
            textExtractor = TextExtractor(negativeText,positiveText)
        else:
            textExtractor = TextExtractor()

        negText, posText = textExtractor.extractFromDataSet()

        self.allWords = textExtractor.dic

        trainFrequencyList = []
        listAllWords = list(self.allWords.keys())
        lenAllWords = len(listAllWords)

        tempDict = {i[1]: i[0] for i in list(enumerate(listAllWords))}

        for i in negText:
            listTemp = [0] * lenAllWords
            for j in i:
                listTemp[tempDict[j]]+=1
            trainFrequencyList.append((listTemp,'N'))

        for i in posText:
            listTemp = [0] * lenAllWords
            for j in i:
                listTemp[tempDict[j]] += 1
            trainFrequencyList.append((listTemp,'P'))

        self.data = trainFrequencyList
