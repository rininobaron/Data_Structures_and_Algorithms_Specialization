def binary_search_dupli(array, number):
	minIndex = 0
	maxIndex = len(array)-1
	index = (maxIndex+minIndex)//2
	while maxIndex>=minIndex:
		if array[index]==number:
			if index==0:
				return index
			if array[index-1]!=number:
				return index
			else:
				maxIndex=index-1
				index = (maxIndex+minIndex)//2
		elif array[index]>number:
			maxIndex = index - 1
			index = (maxIndex+minIndex)//2
		elif array[index]<number:
			minIndex = index + 1
			index = (maxIndex+minIndex)//2
	return -1

def multi_search():
	n = int(input(""))
	array = input("") # array K
	array = array.split(" ")
	array = [int(i) for i in array]
	if len(array) != n:
		print("ERROR!")
		print("The length of the array K is not "+str(n))
	m = int(input(""))
	array2 = input("") # array Q
	array2 = array2.split(" ")
	array2 = [int(i) for i in array2]
	if len(array2) != m:
		print("ERROR!")
		print("The length of the array Q is not "+str(n))
	final_array = []
	for number in array2:
		final_array.append(binary_search_dupli(array, number))
	return print(" ".join([str(i) for i in final_array]))

multi_search()