def majority_element():
	n = int(input(""))
	array = input("")
	array = array.split(" ")
	array = [int(i) for i in array]
	if n != len(array):
		return print("ERROR!\nThe length of array is not "+str(n))
	n_2 = n/2
	array.sort()
	while len(array)>0:
		index = array.index(array[-1])
		count = len(array) - index
		array = array[:index]
		if count > n_2:
			return print(1)
	return print(0)

majority_element()