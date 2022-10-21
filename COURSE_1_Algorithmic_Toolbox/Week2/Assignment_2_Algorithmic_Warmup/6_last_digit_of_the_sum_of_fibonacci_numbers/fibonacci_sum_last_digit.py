def pisano(m):
	Fn_2 = 0
	Fn_1 = 1
	for i in range(m**2):
		Fn = (Fn_2 + Fn_1)%m
		Fn_2, Fn_1 = Fn_1, Fn
		# A Pisano Period starts with 01
		if Fn_2 == 0 and Fn_1 == 1:
			return i + 1

def last_digit_of_the_sum_of_fibos(n):
	n = n%pisano(10)
	if n <= 1:
		return n
	Fn_2 = 0
	Fn_1 = 1
	fibo_sum = 1
	for i in range(2, n+1):
		Fn = (Fn_2 + Fn_1)%10
		Fn_2, Fn_1 = Fn_1, Fn
		fibo_sum += Fn
	return fibo_sum%10

print(last_digit_of_the_sum_of_fibos(int(input(''))))
#print(pisano(int(input(''))))