import os
from project.preprocess.PreProcess import prePreprocess

class TextExtractor:
    def __init__(self, negativeText = '../dataset/competition_SA/neg', positiveText = '../dataset/competition_SA/pos'):
        self.negativeText = negativeText
        self.positiveText = positiveText
        self.dic = {}

    def extractFromDataSet (self):

        return (self.__negativeExtract(),self.__positiveExtract())

    def __negativeExtract(self):

        negativeList = []

        for fileName in os.listdir(self.negativeText):
            arq = open(self.negativeText+ '/' + fileName, 'r')
            list = prePreprocess(arq.read())
            negativeList.append(list)
            for i in list:
                try:
                    self.dic[i]
                except:
                    self.dic[i] = ''
            arq.close()

        return negativeList

    def __positiveExtract(self):

        positiveList = []

        for fileName in os.listdir(self.positiveText):
            arq = open(self.positiveText + '/' + fileName, 'r')
            list = prePreprocess(arq.read())
            positiveList.append(list)
            for i in list:
                try:
                    self.dic[i]
                except:
                    self.dic[i] = ''
            arq.close()
        return positiveList

    def extractTestText(self, pos = '../dataset/testSet/pos', neg = '../dataset/testSet/neg'):

        testText = []

        for fileName in os.listdir(pos):
            arq = open(pos + '/' + fileName, 'r')
            testText.append((prePreprocess(arq.read()),'P'))

        for fileName in os.listdir(neg):
            arq = open(neg + '/' + fileName, 'r')
            testText.append((prePreprocess(arq.read()),'N'))

        return testText

    def extractNewText(self, set = '../dataset/testSet/newSet'):
        testText = []
        for fileName in os.listdir(set):
            arq = open(set + '/' + fileName, 'r')
            testText.append((prePreprocess(arq.read()),''))
        return testText

