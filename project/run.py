from project.knn.knnAlgorithm import Knn
from project.utils.Train import Train
from project.utils import Interface
from project.utils.TextExtractor import TextExtractor
from project.utils.Timer import Timer
from project.validation import Validation

# Interface.msgInitial()
# Interface.msgDataSetInstruction()
# textExtractor = TextExtractor()
# testList = textExtractor.extractNewText(set='dataset/testSet/newTest')
# knn = Knn(Interface.treinner())

# k = int(input('Digite o número de k-vizinhos: '))
# distanceSelector = input('Digite 0 para distância euclidiana ou 1 para distância manhattan. ')
# counter = 1
# timer = Timer()
# for arqTest in testList:
#     print('O arquivo %d foi classificado como: %s\n'%(counter, knn.predict(arqTest[0], k, distanceSelector)))
#     counter+=1
# print('Execution Time: %s\n' % (timer.executionTime()))

def test(ki,kn):

    timeHour = Timer()

    bestF1Measure = float("-inf")
    result = [0, 0]
    textExtractor = TextExtractor()
    testList = textExtractor.extractTestText(pos='dataset/testSet/pos', neg='dataset/testSet/neg')
    knn = Knn(Interface.treinner())

    dist = ['0','1'] #Euclidian/Manhattan

    documentWriteList = []

    for k in range(ki,kn,2):
        print("loading k = %d"%(k))
        for d in dist:
            tp, fp, tn, fn = 0, 0, 0, 0
            timer = Timer()
            for arqTest in testList:
                with open('relatory.txt', 'a') as f:
                    f.write('\n%s best K = %d and best distance = %s.\n'%(timeHour.timeNow(),result[0],result[1]))
                res = knn.predict(arqTest[0],k,d)
                expectedResult = arqTest[1]
                if res == 'P':
                    if expectedResult == 'P':
                        tp+=1
                    else:
                        fp+=1
                else:
                    if expectedResult == 'P':
                        fn+=1
                    else:
                        tn+=1
                #print('resultado esperado %s x resultado do predict %s'%(expectedResult,res))
            if d == '0':
                #print('For K = %d using Euclidian Distance:\n' % k)
                documentWriteList.append('For K = %d using Euclidian Distance:' % k)
            elif d == '1':
                #print('For K = %d using Manhattan Distance:\n' % k)
                documentWriteList.append('For K = %d using Manhattan Distance:' % k)
            #print(' Execution Time: %s\n'%(timer.executionTime()))
            documentWriteList.append(' Execution Time: %s'%(timer.executionTime()))
            f = Validation.generateValidationAnalysis(tp,fp,tn,fn)
            documentWriteList+=f[1]
            if f[0] > bestF1Measure:
                bestF1Measure = f[0]
                result[0] = k
                if d == '0':
                    result[1] = 'Euclidian Distance'
                elif d == '1':
                    result[1] = 'Manhattan Distance'
    documentWriteList.append(('Best Parms are k = %d and distance = %s.'%(result[0],result[1])))
    with open('testReport.txt', 'w') as f:
        for item in documentWriteList:
            f.write("%s\n" % item)
    return ('Best Parms are k = %d and distance = %s.'%(result[0],result[1]))

print(test(3,200))