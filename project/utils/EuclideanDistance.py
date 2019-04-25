import math

#vetor1 = [0, 2, 1, 2]
#vetor2 = [1, 0, 5, 0]

def dist_euclidiana(vetor1, v2):
    dim, add = len(vetor1), 0
    for i in range(dim):
        add += math.pow(vetor1[i] - v2[i], 2)
    return math.sqrt(add)

#print('%.2f' % dist_euclidiana(vetor1, vetor2))
