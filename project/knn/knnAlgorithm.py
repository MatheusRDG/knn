from project.utils.Levensthein import calculateDistance
class Knn:
    def __init__(self, train = []):
        self.train = train

    def predict(self, string, k): #Por conta do sort os empates na distancia serão decididos pelo segundo elemento. O algoritmo tende a N pois lexicograficamente é menor que P.
        distances = []
        for i in self.train:
            distances.append((calculateDistance(string,i[0]),i[2]))
        distances.sort()
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




