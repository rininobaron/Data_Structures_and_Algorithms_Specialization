def calculator(n):
	numCalculations=0
	currentNumber=n
	intermediateNumbers=[str(currentNumber)]
	while currentNumber > 1:
		if currentNumber%3==0:
			currentNumber=currentNumber/3
		elif currentNumber/10==1:
			currentNumber-=1
		elif currentNumber%2==0:
			currentNumber=currentNumber/2
		else:
			currentNumber-=1
		intermediateNumbers.append(str(int(currentNumber)))
		numCalculations+=1
	intermediateNumbers=" ".join(reversed(intermediateNumbers))
	return print(str(numCalculations)+"\n"+intermediateNumbers)

n = int(input())
calculator(n)