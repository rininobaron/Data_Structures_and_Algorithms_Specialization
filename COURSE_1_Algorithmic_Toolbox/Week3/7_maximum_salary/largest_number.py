def largest_concatenate():
	n = int(input(""))
	numbers = input("")
	numbers = numbers.split(" ")
	if n != len(numbers):
		return print("ERROR\nThe numbers are not "+str(n))
	largest_number = ""
	while len(numbers) > 0:
		bestNumber=numbers[0]
		for i,number in enumerate(numbers):
			if i==0:
				continue
			if len(bestNumber) > len(number):
				major=bestNumber
				minor=number
			elif len(bestNumber) < len(number):
				major=number
				minor=bestNumber
			else:
				if bestNumber==number:
					continue
				else:
					major=bestNumber
					minor=number
			if int(major[:len(minor)]) > int(minor):
				bestNumber=major
			elif int(major[:len(minor)]) < int(minor):
				bestNumber=minor
			else:
				for digit in major[len(minor):]:
					if digit > minor[0]:
						bestNumber=major
						break
					else:
						bestNumber=minor
						break
		largest_number+=bestNumber
		numbers.remove(bestNumber)
	return largest_number

print(largest_concatenate())