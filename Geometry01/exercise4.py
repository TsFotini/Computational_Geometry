#exercise 4
from random import seed
from random import randint

class Points: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

class Dataset:
    def __init__(self,data):
        self.data = data
    def leftmostPoint(self):
        mini = 9999
        element = Points(9999,9999)
        for i in self.data:
            if element.x == i.x:
                if element.y < i.y:
                    element = i
            if i.x < mini:
                mini = i.x
                element = i
        return element
    def pos(self,item):
        position = -1
        for i in range(0,len(self.data)):
            if item.x == self.data[i].x and item.y == self.data[i].y:
                position = i
        return position
    def posIndex(self,index):
        return self.data[index]
    def convexhull(self):
        hull = []
        if len(self.data) <3:
            print("There must be at least three points")
        else:
            left = self.leftmostPoint()
            p = self.pos(left)
            while True:
                hull.append(self.posIndex(p))
                q = (p+1)% len(self.data)
                for i in range(0,len(self.data)):
                    if Counterclockwise(self.data[p],self.data[i],self.data[q]) == 1:
                        q=i
                p=q
                if p == self.pos(left):
                    break
        return hull
            

def Counterclockwise(p,q,r):
    values = (q.y-p.y)*(r.x-q.x)-(q.x-p.x)*(r.y-q.y)
    if values < 0:
        return 1        #if counterclockwise
    else:
        return 0        #if not
                    

if __name__ == "__main__":
    allPoints = []
    seed(1)
    for i in range(0,5):
        allPoints.append(Points(randint(0,10),randint(0,10)))
    dataSet = Dataset(allPoints) 
    cnvhull = dataSet.convexhull()
    print("Results:")
    for i in cnvhull:
        print(i.x,i.y)
    

