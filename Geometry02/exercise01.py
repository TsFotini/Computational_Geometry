# -*-Exercise 1
import csv
class Element: 
    def __init__(self,line):
        self.name = line[0]
        self.group = line[len(line)-1]
        line.pop(0)
        line.pop(len(line)-1)
        self.points = line
        self.distance = 0
    def updateDis(self,dis):
        self.distance = dis
        
class Dataset:
    def __init__(self,elements):
        elements.pop(0)
        for el in elements:
            el.points = castToFloat(el.points)
        self.elements = elements
    def printPoints(self):
        for e in self.elements:
            for point in e.points:
                print(point)
        
def csvReader(fileName):
    elements = []
    with open(fileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            element = Element(row)
            elements.append(element)
    return elements
        
def castToFloat(points):
    floatPoints = []
    for i in range(0,len(points)):
        floatPoints.append(float(points[i]))
    return floatPoints
    
if __name__ == "__main__":
    datasetPoints = csvReader('trainingSet.csv')
    dataset = Dataset(datasetPoints)
    dataset.printPoints()
    queries = csvReader('testSet.csv')
    k = input("Enter value of k: ")
    k = int(k)
    
    
