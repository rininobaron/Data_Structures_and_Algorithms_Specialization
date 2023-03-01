def max_number():
	n = int(input(""))
	suma = 0
	numbers = []
	if n==1:
		return 1, str(1)
	if n==2:
		return 1, str(2)
	number = 1
	while suma < n:
		suma+=number
		numbers.append(number)
		# Avoid overcome or repeat number 
		if n-suma<=number:
			suma-=number
			numbers.remove(number)
			numbers.append(n-suma)
			break
		number+=1
	k = len(numbers)
	numbers.sort()
	numbers = [str(int(i)) for i in numbers]
	numbers=" ".join(numbers)
	return k, numbers

k,numbers = max_number()
print(k)
print(numbers)