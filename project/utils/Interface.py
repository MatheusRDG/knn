from project.knn.knnAlgorithm import Knn
from project.utils.Train import Train

def msgInitial ():
    print('Bem-vindo ao knn-Classifier [TextMining 2019.1]')

def msgDataSetInstruction ():
    print('Insira seu dataset neg e pos na pasta knn/project/dataset/competition_SA. Pressione enter para continuar. ')

def verifyExistentOrNewDataSet ():
    verify = input('Digite 0 para usar o treino existente ou 1 para treinar um novo dataset. ')
    while verify != '1' and verify != '0':
        print('Valor inválido')
        verify = input('Digite 0 para usar o treino existente ou 1 para treinar um novo dataset. ')
    return(int(verify))

def verifySaveOrInstantUse ():
    verify = input('Digite 0 usa-lo apenas nesta execução ou 1 para salvar o treino. ')
    while verify != '1' and verify != '0':
        print('Valor inválido')
        verify = input('Digite 0 usa-lo apenas nesta execução ou 1 para salvar o treino. ')
    return(int(verify))

def treinner():
    train = Train()
    while True:
        if verifyExistentOrNewDataSet(): #Treina novo
            train.trainDataSet(negativeText='dataset/competition_SA/neg', positiveText='dataset/competition_SA/pos')
            if verifySaveOrInstantUse():
                train.saveData()
            return train
        else:
            try:
                train.loadData()
                return train
            except EOFError:
                print('Não existe treino salvo.')