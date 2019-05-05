def splitListNParts(list, parts):
    lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    return list(lol(list,parts))

#demonstracao crossVal([i for i in range(100))
def crossVal(_list, N = 10):
	lenghtList = len(_list)
	var = int(lenghtList*N/100)
	cursor = var
	print(_list)
	while cursor <= lenghtList:
		testSet = _list[cursor-var:cursor]
		leftTrain = _list[0:cursor-var]
		rightTrain = _list[cursor:lenghtList]
		cursor+=var
		print('testSet = ' + str(testSet))
		print('leftTrain = ' + str(leftTrain))
		print('rightTrain = ' + str(rightTrain)+ '\n')