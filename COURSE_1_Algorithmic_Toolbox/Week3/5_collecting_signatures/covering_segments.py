def get_points():
	# Get data from user
	n = int(input(""))
	counter = 0
	pairs = []
	while n != counter:
		pair = input("")
		pair = pair.split(" ")
		pair = [int(i) for i in pair]
		if len(pair) != 2:
			return "ERROR!\nThe input is not an integer pair"
		if pair[0] > pair[1]:
			return "ERROR!\nFirst number must be less or equal than second"
		pairs.append(pair)
		counter+=1
	# Sort pairs by r (pair[1]) in ascending order
	pairs_copy = pairs.copy()
	pairs_sort = []
	while len(pairs) > 0:
		pair_min_r = pairs[0]
		target_index = 0
		counter = 0
		for pair in pairs:
			if counter == 0:
				counter+=1
				continue
			if pair[1] < pair_min_r[1]:
				pair_min_r = pair
				target_index = counter
			if pair[1] == pair_min_r[1]:
				if pair[0] < pair_min_r[0]:
					pair_min_r = pair
					target_index = counter
			counter+=1
		pairs_sort.append(pair_min_r)
		pairs.pop(target_index)
	#print(pairs_sort)
	# Get points
	final_points = []
	while len(pairs_sort)>0:
		temp_agg = []
		pair_ref = pairs_sort[0]
		for pair in pairs_sort:
			if pair_ref[1] >= pair[0] and pair_ref[1] <= pair[1]:
				temp_agg.append(pair)
		final_point = temp_agg[0][1]
		for pair in temp_agg:
			pairs_sort.remove(pair)
		final_points.append(final_point)
	return final_points

final_points = get_points()
len_ = len(final_points)
final_points = " ".join([str(i) for i in final_points])
print(len_)
print(final_points)