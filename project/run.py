from project.knn.knnAlgorithm import Knn
from project.utils.Train import Train
from project.utils import Interface

Interface.msgInitial()
Interface.msgDataSetInstruction()
knn = Knn(Interface.treinner().data)
while True:
    string = input('Digite a palavra a ser rotulada ou 0 para encerrar: ')
    if string == '0':
        break
    while True:
        try:
            k = int(input('Digite a quantidade de vizinhos a ser considerada: '))
            break
        except:
            print('Valor inválido')
    print(knn.predict(string,k))