def count_swaps(array):
	array2=[]
	counter=0
	while len(array)>0:
		minIndex=0
		for j in range(1,len(array)):
			if array[j] < array[minIndex]:
				minIndex=j
		if minIndex==0:
			array2.append(array[minIndex])
			array.remove(array[minIndex])
		else:
			array2.append(array[minIndex])
			array.remove(array[minIndex])
			counter+=minIndex
	return counter

def counter():
	n=int(input(""))
	array=input("")
	array=array.split(" ")
	array=[int(i) for i in array]
	if len(array)!=n:
		return print("ERROR!\nThe length of array is not "+str(n))
	counter=count_swaps(array)
	return print(counter)

counter()