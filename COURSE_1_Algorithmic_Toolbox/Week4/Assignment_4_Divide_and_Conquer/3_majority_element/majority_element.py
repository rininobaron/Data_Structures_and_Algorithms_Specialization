def majority_element():
	n = int(input(""))
	array = input("")
	array = array.split(" ")
	array = [int(i) for i in array]
	if n != len(array):
		return print("ERROR!\nThe length of array is not "+str(n))
	n_2 = n/2
	while len(array)>0:
		pivot = array[0]
		suma=0
		counter=0
		len_ref=len(array)
		while len_ref>counter:
			number=array[0]
			if number==pivot:
				suma+=1
				if suma>n_2:
					return print(1)
			array.remove(number)
			counter+=1
	return print(0)

majority_element()