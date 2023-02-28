def max_number():
	n = int(input(""))
	suma = 0
	numbers = []
	if n%2 == 0:
		number = n/2
		numbers.append(number)
		suma=number
		while suma != n:
			number-=1
			suma+=number
			if suma > n:
				suma-=number
				continue
			numbers.append(number)
	else:
		number = n/2+1
		numbers.append(number)
		suma=number
		while suma != n:
			number-=1
			suma+=number
			if suma > n:
				suma-=number
				continue
			numbers.append(number)
	k = len(numbers)
	numbers = [str(int(i)) for i in numbers]
	numbers=" ".join(numbers)
	return k,numbers

k,numbers = max_number()
print(k)
print(numbers)