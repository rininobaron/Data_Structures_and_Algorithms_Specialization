def largest_concatenate():
	n = int(input(""))
	numbers = input("")
	numbers = numbers.split(" ")
	if n != len(numbers):
		return print("ERROR\nThe numbers are not "+str(n))
	numbers2=[]
	for number in numbers:
		for digit in number:
			numbers2.append(digit)
	numbers2 = [int(i) for i in numbers2]
	largest_number = ""
	while len(numbers2) > 0:
		temp=max(numbers2)
		largest_number+=str(temp)
		numbers2.remove(temp)
	return largest_number

print(largest_concatenate())