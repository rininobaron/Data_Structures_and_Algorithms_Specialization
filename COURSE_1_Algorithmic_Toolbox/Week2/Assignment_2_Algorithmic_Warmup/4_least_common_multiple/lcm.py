def lcm(a, b):
	if a == 0 or b == 0:
		return max(a, b)
	current_lcm = max(a, b)
	while (current_lcm%a != 0) or (current_lcm%b != 0):
		if current_lcm%a != 0:
			current_lcm += (a - current_lcm%a)
		elif current_lcm%b != 0:
			current_lcm += (b - current_lcm%b)
	return current_lcm

a, b = map(int, input().split())
print(lcm(a, b))