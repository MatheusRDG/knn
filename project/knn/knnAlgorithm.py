from project.utils.EuclideanDistance import dist_euclidiana
from project.utils.Train import Train
class Knn:
    def __init__(self, train = Train()):
        self.train = train

    def predict(self, document, k):
        freqListDoc = self.createFrequencyList(document)
        distances = []
        for i in self.train.data:
            distances.append((dist_euclidiana(i[0],freqListDoc),i[1]))
        distances.sort()
        #print(distances)
        n, p = 0, 0
        for i in range(k):
            try:
                if distances[i][1] == 'N':
                    n+=1
                else:
                    p+=1
            except IndexError:
                print('Train lenght is small than k neighbors.')
        print('positive = %d, negative = %d'%(p,n))
        if p > n:
            return('P')
        else:
            return('N')

    def createFrequencyList(self, document):
        lenAllWords = len(self.train.allWords)
        listTemp = [0] * lenAllWords
        listAllWords = list(self.train.allWords.keys())
        for i in range(lenAllWords):
            listTemp[i] = document.count(listAllWords[i])
        return listTemp



