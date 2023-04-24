def calculator(n):
	numCalculations=0
	currentNumber=1
	intermediateNumbers=[currentNumber]
	while currentNumber < n:
		if currentNumber<=n/3:
			currentNumber=3*currentNumber
			intermediateNumbers.append(currentNumber)
		elif currentNumber<=n/2:
			currentNumber=2*currentNumber
			intermediateNumbers.append(currentNumber)
		else:
			currentNumber+=1
			intermediateNumbers.append(currentNumber)
		numCalculations+=1
	intermediateNumbers=" ".join([str(i) for i in intermediateNumbers])
	return print(str(numCalculations)+"\n"+intermediateNumbers)

n = int(input())
calculator(n)