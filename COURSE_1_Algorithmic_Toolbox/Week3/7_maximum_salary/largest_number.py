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
			bestNumber=isBetter(number,bestNumber)
		largest_number+=bestNumber
		numbers.remove(bestNumber)
	return largest_number

def isBetter(number1,number2):
	num1 = number1+number2
	num2 = number2+number1
	if str(max(int(num1),int(num2))) == num1:
		return number1
	else:
		return number2

print(largest_concatenate())