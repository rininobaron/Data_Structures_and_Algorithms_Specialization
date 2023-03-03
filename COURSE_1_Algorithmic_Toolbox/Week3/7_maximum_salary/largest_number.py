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
				temp=major[len(minor):]
				temp=[int(digit) for digit in temp]
				major_max=max(temp)
				minor_max=max([int(digit) for digit in minor])
				if major_max > minor_max:
					bestNumber=major
				else:
					bestNumber=minor
		largest_number+=bestNumber
		numbers.remove(bestNumber)
	return largest_number

print(largest_concatenate())