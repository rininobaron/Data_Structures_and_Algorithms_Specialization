def counter():
    n, m = map(int, input().split(" "))
    array=[]
    for _ in range(n):
        l, r = map(int, input().split(" "))
        array.append([int(l),"l"])
        array.append([int(r),"r"])
    points = input().split(" ")
    if len(points) != m:
        return print(f"ERROR!\nThe number of points are not {m}")
    for point in points:
        array.append([int(point),"p"])
    array.sort()
    segments=0
    counter_dict={}
    for item in array:
        if item[1]=="l":
            segments+=1
        elif item[1]=="r":
            segments-=1
        else:
            counter_dict[str(item[0])]=counter_dict.get(str(item[0]),0)+segments
    counter_list=[str(counter_dict[str(point)]) for point in points]
    return print(" ".join(counter_list))

counter()
