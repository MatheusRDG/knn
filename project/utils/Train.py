import pickle
from project.utils.TextExtractor import TextExtractor
class Train:
    def __init__(self, data = []):
        self.data = data

    def saveData(self):
        with open('train.txt', 'wb') as fp:
            pickle.dump(self.data, fp)

    def loadData(self):
        with open('train.txt', 'rb') as fp:
            self.data = pickle.load(fp)

    def trainDataSet(self, negativeText = False, positiveText = False):
        if negativeText:
            textExtractor = TextExtractor(negativeText,positiveText)
        else:
            textExtractor = TextExtractor()
        self.data = textExtractor.extractFromDataSet()

