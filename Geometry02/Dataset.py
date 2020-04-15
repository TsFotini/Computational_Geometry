# -*- Dataset Module
import csv
from functions import euclidean,castToFloat,splitFile,getheadData 
 

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
    def updateGroup(self,grp):
        self.group = grp
        
class Dataset:
    def __init__(self,elements):
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
    elements.pop(0)
    return elements

def csvSplitReader(filename,rowNum,startOrEnd):
    elements = []
    content = splitFile(filename,rowNum,startOrEnd)
    for item in content:
        element = Element(item)
        elements.append(element)
    return elements

def classify(dataset,query,k):
    scoreKeeper = []
    for el in dataset.elements:
        dis = euclidean(el.points,query.points)
        el.updateDis(dis)
    up = dataset.elements
    up.sort(key=lambda item: item.distance , reverse=False)
    for i in range(0,k):
        scoreKeeper.append(up[i].group)
    res = max(set(scoreKeeper), key = scoreKeeper.count)
    query.updateGroup(res)
    
def predictions(queryset,filename):
    header = getheadData(filename)
    with open("predict.csv", 'w', newline='') as myfile:
        for i in range(0,len(queryset.elements)):
            queryset.elements[i].points.append(queryset.elements[i].group)
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(header)
        for i in queryset.elements:
            wr.writerow(i.points)