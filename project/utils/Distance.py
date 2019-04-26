def selectDistance(selector):
    if selector == '0':
        return dist_Euclidian
    elif selector == '1':
        return dist_Manhattan

def dist_Euclidian(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += (v1[i] - v2[i]) ** 2
    return res**0.5

def dist_Manhattan(v1,v2):
    res = 0
    for i in range(len(v1)):
        res += abs(v1[i] - v2[i])
    return res
