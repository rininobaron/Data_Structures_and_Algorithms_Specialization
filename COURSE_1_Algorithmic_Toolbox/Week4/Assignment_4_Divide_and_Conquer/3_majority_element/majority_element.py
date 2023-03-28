def majority_element():
	n = int(input(""))
	array = input("")
	array = array.split(" ")
	array = [int(i) for i in array]
	if n != len(array):
		return print("ERROR!\nThe length of array is not "+str(n))
	n_2 = n/2
	array_set = set(array)
	for number in array_set:
		if array.count(number) > n_2:
			return print(1)
	return print(0)

majority_element()