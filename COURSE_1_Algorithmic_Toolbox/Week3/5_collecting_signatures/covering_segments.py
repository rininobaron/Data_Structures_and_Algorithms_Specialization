def get_points():
	# Get data from user
	n = int(input(""))
	counter = 0
	pairs = []
	# From segment with min l
	min_l = 10**9
	min_r = 0 # Not necessary the min r
	index_min = 0
	# From segment with max r
	max_l = 0 # Not necessary the max l
	max_r = 0
	index_max = 0
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
		if pair[0] < min_l:
			min_l = pair[0]
			min_r = pair[1]
			index_min = counter
		if pair[1] > max_r:
			max_l = pair[0]
			max_r = pair[1]
			index_max = counter
	# Point sweep
	dict_points = {}
	for point in range(min_l, max_r+1):
		counter = 0
		for pair in pairs:
			if pair[0] <= point and pair[1] >= point:
				if point not in dict_points.keys():
					dict_points[point] = []
				dict_points[point].append(counter)
			counter+=1
	# Get point with embrace more segmnts
	max_point = 0 # The point with MORE SEGMENTS
	target_len = 0 # Number of segements of the max_point
	for point in dict_points.keys():
		if target_len <= len(dict_points[point]):
			if max_point < point:
				target_len = len(dict_points[point])
				max_point = point
	final_points = [max_point]
	segment_indexes = list(range(len(pairs)))
	hola = segment_indexes.copy()
	for i in dict_points[max_point]:
		segment_indexes.remove(i)
	# Get remain points
	while len(segment_indexes) > 0:
		temp_dict = {}
		for point in dict_points.keys():
			if point in final_points:
				continue
			for index in segment_indexes:
				if index in dict_points[point]:
					if point not in temp_dict.keys():
						temp_dict[point] = []
					temp_dict[point].append(index)
		max_point = 0
		target_len = 0
		for point in temp_dict.keys():
			if target_len <= len(temp_dict[point]):
				if max_point < point:
					target_len = len(temp_dict[point])
					max_point = point
		for i in temp_dict[max_point]:
			segment_indexes.remove(i)
		final_points.append(max_point)
	final_points.sort()
	return final_points

final_points = get_points()
len_ = len(final_points)
final_points = " ".join([str(i) for i in final_points])
print(len_)
print(final_points)