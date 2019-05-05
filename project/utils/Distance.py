from decimal import Decimal

def selectDistance(selector): #['euclidean', 'manhattan', 'minkowski', 'cosine', 'jaccard']

    if selector == 'euclidean':
        return dist_Euclidean
    elif selector == 'manhattan':
        return dist_Manhattan
    elif selector == 'cosine':
        return dist_Cosine
    elif selector == 'minkowski':
        return dist_Minkowski
    elif selector == 'jaccard':
        return dist_Jaccard

def dist_Euclidean(x, y):

    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i]) ** 2
    return res**0.5

def dist_Manhattan(x, y):

    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def dist_Cosine(x, y):

    def square_rooted(x):
        return round((sum([a * a for a in x])) ** 0.5, 3)

    numerator = sum(a * b for a, b in zip(x, y))
    denominator = square_rooted(x) * square_rooted(y)
    return round(numerator / float(denominator), 3)

def dist_Minkowski(x,y,p_value = 3): #p = 1 manhatan, p = 2 euclidian

    def nth_root(value, n_root):
        root_value = 1 / float(n_root)
        return round(Decimal(value) ** Decimal(root_value), 3)

    return nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)

def dist_Jaccard(x, y):

    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality / float(union_cardinality)
