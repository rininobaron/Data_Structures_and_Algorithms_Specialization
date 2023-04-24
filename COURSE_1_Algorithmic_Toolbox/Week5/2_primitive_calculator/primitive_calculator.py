def calculator(n):
	numCalculations=0
	currentNumber=n
	intermediateNumbers=[str(currentNumber)]
	while currentNumber > 1:
		if currentNumber/10==1:
			currentNumber-=1
		elif currentNumber%2==0:
			if currentNumber==4:
				currentNumber-=1
			else:
				currentNumber=currentNumber/2
		elif currentNumber%3==0:
			currentNumber=currentNumber/3
		else:
			currentNumber-=1
		intermediateNumbers.append(str(int(currentNumber)))
		numCalculations+=1
	intermediateNumbers=" ".join(reversed(intermediateNumbers))
	return print(str(numCalculations)+"\n"+intermediateNumbers)

n = int(input())
calculator(n)