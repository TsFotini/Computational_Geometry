# -*Functions Module
import math

def castToFloat(points):
    floatPoints = []
    for i in range(0,len(points)):
        floatPoints.append(float(points[i]))
    return floatPoints

def euclidean(point1,point2):
    sumation = 0.0
    if len(point1) != len(point2):
        print("Not the same dimension")
        return -1
    else:
        for i in range(0,len(point1)):
            diff = point1[i] - point2[i]
            sumation = pow(diff,2) + sumation
    return math.sqrt(sumation)
               


