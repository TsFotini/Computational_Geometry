# -*Functions Module
import math
import pandas as pd

def castToFloat(points):
    floatPoints = []
    for i in range(0,len(points)):
        floatPoints.append(float(points[i]))
    return floatPoints

def splitFile(filename,rowNum,startOrEnd):
    data = pd.read_csv(filename)
    rowList = []
    if startOrEnd == "start":
        df = data.head(rowNum)
        rowList = df.values.tolist()
    else:
        df = data.tail(rowNum)
        rowList = df.values.tolist()
    return rowList

def getheadData(filename):
    data = pd.read_csv(filename)
    header = data.columns.tolist()
    header.pop(0)
    return header
        
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
               


