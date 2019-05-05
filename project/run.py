from project.knn.knnAlgorithm import Knn
from project.utils.Train import Train
from project.utils import Interface
from project.utils.TextExtractor import TextExtractor
from project.utils.Timer import Timer
from project.validation import Validation
from project.utils.AuxMethods import splitListNParts
from random import randint

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

def crossValidation(N=10, maxK=11):
    # ExtractText From dataset
    textExtractor = TextExtractor(negativeText='dataset/competition_SA/neg',
                                  positiveText='dataset/competition_SA/pos')
    print("Extraindo texto")
    posList, negList = textExtractor.extractFromDataSet()

    # CrossValidation Config
    lenghtList = len(posList)
    division = int(lenghtList * N / 100)
    cursor = division

    # Test Config
    bestF1Measure = float('inf')
    result = [0, 0]
    distances = ['euclidean', 'manhattan', 'minkowski', 'cosine', 'jaccard']
    timeRegister = Timer()

    print("Iniciando CrossValidation")
    while cursor <= lenghtList:
        print("Executando nova partição - cursor = %d" % cursor)
        # positiveDivision
        positiveTest = posList[cursor - division:cursor]
        positiveTrain = posList[0:cursor - division] + posList[cursor:lenghtList]  # left + right

        # negativeDivision
        negativeTest = negList[cursor - division:cursor]
        negativeTrain = negList[0:cursor - division] + negList[cursor:lenghtList]  # left + right

        # testList
        testList = [(i, 'P') for i in positiveTest] + [(i, 'N') for i in negativeTest]

        cursor += division
        # treinar com esses tests #rodar os tests

        # Knn Config
        print("Iniciando treino da partição")
        train = Train()
        train.trainWithSpecifiedSet(positiveTrain=positiveTrain, negativeTrain=negativeTrain)
        knn = Knn(train)

        # K test
        print("Iniciando tests KNN da partição")
        for k in range(3, maxK + 1, 2):

            for distance in distances:

                print("loading k = %d and distance = %s" % (k, distance))

                tp, fp, tn, fn = 0, 0, 0, 0

                for doc in testList:

                    res = knn.predict(doc[0], k, distance)

                    expectedResult = doc[1]

                    if res == 'P':

                        if expectedResult == 'P':
                            tp += 1
                        else:
                            fp += 1
                    else:

                        if expectedResult == 'P':
                            fn += 1
                        else:
                            tn += 1

                f = Validation.generateValidationAnalysis(tp, fp, tn, fn)

                documentWriteList = ['Using k = %d and distance = %s: ' % (k, distance)]
                documentWriteList += f[1]

                with open('testReport.txt', 'a') as f:
                    for item in documentWriteList:
                        f.write("%s\n" % item)
                    f.write('\n')

                if f[0] > bestF1Measure:
                    bestF1Measure = f[0]
                    result[0] = k
                    result[1] = distance

    return ('Best Parms are k = %d and distance = %s.' % (result[0], result[1]))


# def testBestParms(ki, kn):
#     timeRegister = Timer()
#
#     bestF1Measure = float("-inf")
#
#     result = [0, 0]
#
#     textExtractor = TextExtractor()
#     testList = textExtractor.extractTestText(pos='dataset/testSet/pos', neg='dataset/testSet/neg')
#     knn = Knn(Interface.treinner())
#
#     distances = ['euclidean', 'manhattan', 'minkowski', 'cosine', 'jaccard']  # Euclidian/Manhattan
#
#     documentWriteList = []
#
#     for k in range(ki, kn, 2):
#         print("loading k = %d" % (k))
#
#         with open('relatory.txt', 'a') as f:
#             f.write('\n%s best K = %d and best distance = %s.\n' % (timeRegister.timeNow(), result[0], result[1]))
#
#         for d in dist:
#
#             tp, fp, tn, fn = 0, 0, 0, 0
#             timer = Timer()
#
#             for arqTest in testList:
#                 res = knn.predict(arqTest[0], k, d)
#                 expectedResult = arqTest[1]
#                 if res == 'P':
#                     if expectedResult == 'P':
#                         tp += 1
#                     else:
#                         fp += 1
#                 else:
#                     if expectedResult == 'P':
#                         fn += 1
#                     else:
#                         tn += 1
#
#             if d == '0':
#                 documentWriteList.append('For K = %d using Euclidian Distance:' % k)
#             elif d == '1':
#                 documentWriteList.append('For K = %d using Manhattan Distance:' % k)
#             documentWriteList.append(' Execution Time: %s' % (timer.executionTime()))
#
#             f = Validation.generateValidationAnalysis(tp, fp, tn, fn)
#             documentWriteList += f[1]
#             if f[0] > bestF1Measure:
#                 bestF1Measure = f[0]
#                 result[0] = k
#                 if d == '0':
#                     result[1] = 'Euclidian Distance'
#                 elif d == '1':
#                     result[1] = 'Manhattan Distance'
#
#     documentWriteList.append(('Best Parms are k = %d and distance = %s.' % (result[0], result[1])))
#     with open('testReport.txt', 'w') as f:
#         for item in documentWriteList:
#             f.write("%s\n" % item)
#     return ('Best Parms are k = %d and distance = %s.' % (result[0], result[1]))


print(crossValidation())
