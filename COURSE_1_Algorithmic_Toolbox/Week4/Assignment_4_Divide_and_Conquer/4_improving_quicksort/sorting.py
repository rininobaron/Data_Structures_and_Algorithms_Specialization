def sort_custom():
	n=int(input(""))
	array=input("")
	array=array.split(" ")
	array=[int(i) for i in array]
	if len(array)!=n:
		return print("ERROR!\nThe length of array is not "+str(n))
	counter_dict={}
	for number in array:
		if number not in counter_dict.keys():
			counter_dict[number]=0
		counter_dict[number]+=1
	keys_sorted=list(counter_dict.keys())
	keys_sorted.sort()
	array=[]
	for key in keys_sorted:
		array+=[key]*counter_dict[key]
	array=[str(i) for i in array]
	return print(" ".join(array))

sort_custom()