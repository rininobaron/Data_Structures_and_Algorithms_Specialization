def majority_element():
	n = int(input(""))
	array = input("")
	array = array.split(" ")
	array = [int(i) for i in array]
	if n != len(array):
		return print("ERROR!\nThe length of array is not "+str(n))
	n_2 = n/2
	counter=0
	pivots=[]
	while len(array)>counter:
		pivot = array[counter]
		if pivot in pivots:
			counter+=1
			continue
		pivots.append(pivot)
		suma=0
		for number in array:
			if number==pivot:
				suma+=1
				if suma>n_2:
					return print(1)
		counter+=1
	return print(0)

majority_element()