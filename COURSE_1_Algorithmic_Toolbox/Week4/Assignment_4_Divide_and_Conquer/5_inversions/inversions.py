def merge(array1, array2):
	counter=0
	while len(array1)>0 and len(array2)>0:
		if array1[0]<=array2[0]:
			array1.remove(array1[0])
			continue
		counter+=len(array1)
		array2.remove(array2[0])
	return counter

def sort_count_swaps(array):
	counter=0
	array_sorted=sorted(array)
	for i in range(len(array_sorted)):
		j=array.index(array_sorted[i])+i
		array.remove(array_sorted[i])
		counter+=abs(i-j)
	return array_sorted, counter

def counter():
	n=int(input(""))
	array=input("")
	array=array.split(" ")
	array=[int(i) for i in array]
	if len(array)!=n:
		return print("ERROR!\nThe length of array is not "+str(n))
	m=len(array)//2
	array1=array[:m].copy()
	array2=array[m:].copy()
	array1,counter1=sort_count_swaps(array1)
	array2,counter2=sort_count_swaps(array2)
	counter=merge(array1,array2)
	return print(counter+counter1+counter2)

counter()