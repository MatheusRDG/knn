def generateValidationAnalysis(tp, fp, fn, tn):
    confusionMatrix = generateConfusionMatrix(tp,fp,fn,tn)
    l = [[str(i) for i in j] for j in confusionMatrix]
    precision = (' Precision = %.2f%%'%(calculatePrecision(confusionMatrix)*100))
    recall = (' Recall = %.2f%%' % (calculateRecall(confusionMatrix)*100))
    accuracy = (' Accuracy = %.2f%%' % (calculateAccuracy(confusionMatrix)*100))
    f = (calculateF1Measure(confusionMatrix))
    fm =(' F1-Measure = %.2f\n' % f)
    writeList = [' Confusion Matrix:', '  +  -', (' + ' + '  '.join(l[0])), (' - ' + '  '.join(l[1])),
                 precision, recall, accuracy, fm]
    return (f,writeList)

def generateConfusionMatrix(tp, fp, fn, tn):
    return [[tp,fp],[fn,tn]]

def calculatePrecision(confusionMatrix):
    den = (confusionMatrix[0][0] + confusionMatrix[0][1])
    if den == 0:
        return 0
    return confusionMatrix[0][0]/den

def calculateRecall(confusionMatrix):
    den = (confusionMatrix[0][0] + confusionMatrix[1][0])
    if den == 0:
        return 0
    return confusionMatrix[0][0]/den

def calculateAccuracy(confusionMatrix):
    den = (confusionMatrix[0][0]+confusionMatrix[0][1]+confusionMatrix[1][0]+confusionMatrix[1][1])
    if den == 0:
        return 0
    return (confusionMatrix[0][0]+confusionMatrix[1][1])/den

def calculateF1Measure(confusionMatrix):
    precision = calculatePrecision(confusionMatrix)
    recall = calculateRecall(confusionMatrix)
    den = (precision+recall)
    if den == 0:
        return 0
    return 2*((precision*recall)/den)


