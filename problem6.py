from math import sqrt

point1 = [20.9, 15.3, 20.4]
point2 = [0.6, 34.7, 8.1]
point3 = [12.1, 15.8, 2.3]
point4 = [15.0, 5.8, 16.9]
origin = [0,0,0]

def euclidean_distance(list1, list2):
    
    # use area in set to subtract

    x_brackets = (list1[0] - list2[0])**2
    y_brackets = (list1[1] - list2[1])**2
    z_brackets = (list1[2] - list2[2])**2

    d = sqrt((x_brackets + y_brackets + z_brackets))

    print(d)


# Find the distance from each point to the origin

print("origin to 1")
euclidean_distance(origin,point1)
print("origin to 2")
euclidean_distance(origin,point2)
print("origin to 3") # Results resulting in this being the closest at 20.33
euclidean_distance(origin,point3)
print("origin to 4")
euclidean_distance(origin,point4)

#Find the distance between points

print("point 1 - point 2")
euclidean_distance(point1,point2)
print("point 1 - point 3")
euclidean_distance(point1,point3)
print("point 1 - point 4") 
euclidean_distance(point1,point4)
print("point 2 - point 3")
euclidean_distance(point2,point3)
print("point 2 - point 4")
euclidean_distance(point2,point4)
print("point 3 - point 4")
euclidean_distance(point3,point4)