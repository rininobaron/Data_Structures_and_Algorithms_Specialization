def largest_concatenate():
	n = int(input(""))
	numbers = input("")
	numbers = numbers.split(" ")
	if n != len(numbers):
		return print("ERROR\nThe numbers are not "+str(n))
	largest_number = ""
	while len(numbers) > 0:
		fullNumber = numbers[0]
		maxNumber = numbers[0][0]
		for i,number in enumerate(numbers):
			if i==0:
				continue
			if int(number[0]) > int(maxNumber):
				fullNumber=number
				maxNumber=number[0]
			elif int(number[0]) == int(maxNumber):
				if int(number[-1]) > int(fullNumber[-1]):
					fullNumber=number
					maxNumber=number[0]
		largest_number+=fullNumber
		numbers.remove(fullNumber)
	return largest_number

print(largest_concatenate())