from project.knn.knnAlgorithm import Knn
from project.utils.Train import Train
print('Bem-vindo ao knn-Classifier [TextMining 2019.1]\nDigite 0 para usar o treino existente ou 1 para treinar um novo dataset. ')
if int(input()):
    input('Insira seu dataset neg e pos na pasta knn/project/dataset/competition_SA. Pressione enter para continuar. ')
    train = Train()
    train.trainDataSet(negativeText = 'dataset/competition_SA/neg', positiveText = 'dataset/competition_SA/pos')
    knn = Knn(train.data)
    if int(input('Digite 0 para salvar o treino ou 1 para usa-lo apenas nesta execução. ')):
        pass
    else:
        train.saveData()
else:
    train = Train()
    train.loadData()
    knn = Knn(train.data)
while True:
    string = input('Digite a palavra a ser rotulada ou 0 para encerrar: ')
    if string == '0':
        break
    k = int(input('Digite a quantidade de vizinhos a ser considerada: '))
    print(knn.predict(string,k))