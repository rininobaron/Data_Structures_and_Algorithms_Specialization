def counter():
    n, m = map(int, input().split(" "))
    l_array,r_array=[],[]
    for _ in range(n):
        l, r = map(int, input().split(" "))
        l_array.append(l)
        r_array.append(r)
    points = input().split(" ")
    points_int=[int(i) for i in points]
    if len(points) != m:
        return print(f"ERROR!\nThe number of points are not {m}")
    map_ref=[]
    for point in points_int:
        for l,r in zip(l_array,r_array):
            map_ref.append([point,sorted([l,r,point])])
    counter_dict={point:0 for point in points}
    for array in map_ref:
        if array[0]==array[1][1]:
            counter_dict[str(array[0])]+=1
    return print(" ".join([str(i) for i in counter_dict.values()]))

counter()
