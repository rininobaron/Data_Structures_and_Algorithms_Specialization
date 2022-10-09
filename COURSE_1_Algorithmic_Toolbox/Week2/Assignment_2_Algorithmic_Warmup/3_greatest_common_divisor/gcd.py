def huge_fibo_number(tupla):
	n = int(tupla[0])
	m = int(tupla[1])
	if n <= 1:
		return n
	final_gcd = 1
	for d in range(2, min(n, m) * 1):
		if n%d == 0 and m%d == 0:
			if final_gcd < d:
				final_gcd = d
	return final_gcd
print(huge_fibo_number(input('').split(' ')))