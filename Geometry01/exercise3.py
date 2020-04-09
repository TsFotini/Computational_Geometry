#exercise 3
from random import seed
from random import randint

class Points: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

class Dataset:
    def __init__(self,data):
        self.data = data
    def upper(self):
        up = self.data
        up.sort(key=lambda item: (item.x, item.y) , reverse=False)
        return up
    def down(self):
        dn = self.data
        dn.sort(key=lambda item: (item.x, item.y) , reverse=True)
        return dn 
    def listConvexHull(self,sortedList):
        lists = []
        lists.append(sortedList[0])
        lists.append(sortedList[1])
        for i in range(2,len(sortedList)-1):
            lists.append(sortedList[i])
            while len(lists) > 2 and orient(lists[len(lists)-1],lists[len(lists)-2],lists[len(lists)-3])==1:
                lists.pop(len(lists)-2)
        return lists
    def IncConvexHull(self):
        sortedUplist = self.upper()
        UpperList = self.listConvexHull(sortedUplist)
        sortedDownlist = self.down()
        DownList = self.listConvexHull(sortedDownlist)
        for i in DownList:
            UpperList.append(i)
        return UpperList
        
        
def printLists(lists):
    print("Results:")
    for i in lists:
        print("(",i.x,",",i.y,")")

def orient(p,q,r):
    values = (q.y-p.y)*(r.x-q.x)-(q.x-p.x)*(r.y-q.y)
    if values < 0:
        return 1        #if counterclockwise
    else:
        return 0        #if not
        
if __name__ == "__main__":
    points = [] 
    seed(1)
    for i in range(0,7):
       points.append(Points(randint(0,10),randint(0,10)))
    points.append(Points(0, 3)) 
    points.append(Points(2, 2)) 
    points.append(Points(1, 1)) 
    points.append(Points(2, 1)) 
    points.append(Points(3, 0)) 
    points.append(Points(0, 0)) 
    points.append(Points(3, 3))
    dataSet = Dataset(points)
    printLists(dataSet.IncConvexHull())