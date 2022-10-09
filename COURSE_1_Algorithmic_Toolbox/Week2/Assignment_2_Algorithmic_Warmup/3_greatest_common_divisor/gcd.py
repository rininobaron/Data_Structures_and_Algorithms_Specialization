def huge_fibo_number(tupla):
	n = int(tupla[0])
	m = int(tupla[1])
	if n <= 1:
		return n%m
	Fn_2 = 0
	Fn_1 = 1
	for _ in range(n-1):
		Fn = Fn_2 + Fn_1
		#Fn = Fn%10
		Fn_2, Fn_1 = Fn_1, Fn
	return Fn%m
print(huge_fibo_number(input('').split(' ')))