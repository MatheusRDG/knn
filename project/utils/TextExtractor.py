import os
from project.preprocess.PreProcess import preProcess

#thread
class TextExtractor:
    def __init__(self, negativeText = '../dataset/competition_SA/neg', positiveText = '../dataset/competition_SA/pos'):
        self.negativeText = negativeText
        self.positiveText = positiveText

    def extractFromDataSet (self):

        #negativeExtract = threading.Thread(target=self.__negativeExtract, args=())
        #positiveExtract = threading.Thread(target=self.__positiveExtract,args=())

        #negativeExtract.start()
        #positiveExtract.start()

        #while negativeExtract.is_alive() or positiveExtract.is_alive():
        #    time.sleep(1)

        #return (negativeExtract,positiveExtract)

        return self.__negativeExtract()+self.__positiveExtract()

    def __negativeExtract(self):

        negativeList = []

        for fileName in os.listdir(self.negativeText):
            arq = open(self.negativeText+ '/' + fileName, 'r')
            negativeList+=(preProcess(arq.read()))
            arq.close()

        return list(map(lambda k: (k[0],k[1],'N'), [j for i in negativeList for j in i]))

    def __positiveExtract(self):

        positiveList = []

        for fileName in os.listdir(self.positiveText):
            arq = open(self.positiveText+ '/' + fileName, 'r')
            positiveList+=(preProcess(arq.read())) #To separe in files -> positiveList.append(preProcess(arq.read()))
            arq.close()

        return list(map(lambda k: (k[0],k[1],'P'), [j for i in positiveList for j in i])) #To separe in sentence -> positiveList

#textExtractor = TextExtractor()
#print(textExtractor.extractFromDataSet())