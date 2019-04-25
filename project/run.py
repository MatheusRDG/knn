from project.knn.knnAlgorithm import Knn
from project.utils.Train import Train
from project.utils import Interface
from project.utils.TextExtractor import TextExtractor
from project.utils.Timer import Timer
Interface.msgInitial()
Interface.msgDataSetInstruction()
#
timer = Timer()
textExtractor = TextExtractor()
testList = textExtractor.extractTestText(pos='dataset/testSet/pos',neg = 'dataset/testSet/neg')
print('Tempo de execução = '+ timer.executionTime())
#TESTE
knn = Knn(Interface.treinner())
print('Tempo de treinamento = '+ timer.executionTime())
#TESTE
for i in testList:
    #print(i)
    print(knn.predict(i[0],31))
    print(i[1])
print('Tempo de teste = '+ timer.executionTime())
# while True:
#     string = input('Digite a palavra a ser rotulada ou 0 para encerrar: ')
#     if string == '0':
#         break
#     while True:
#         try:
#             k = int(input('Digite a quantidade de vizinhos a ser considerada: '))
#             break
#         except:
#             print('Valor inválido')
#     print(knn.predict(string,k))