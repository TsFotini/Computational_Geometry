# Exercise 1*-
class Points:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
def printList(triangle):
    print("List has :")
    for i in triangle:
        print(i.x)
        print(i.y)
        print("\n")

def IfTriangle(triangle,printAnswer):
    result = (triangle[1].y-triangle[2].y)*triangle[0].x + (triangle[2].y-triangle[0].y)*triangle[1].x + (triangle[0].y-triangle[1].y)*triangle[2].x
    #result = (y2-y3)*x1 + (y3-y1)*x2 + (y1-y2)*x3
    result = result * 0.5
    if printAnswer == 1:
        if result == 0:
            print ("No") 
        else:
            print("Yes")
    return abs(result)

def OriginIncluded(triangle):
    result = IfTriangle(triangle,0)
    temp = triangle.copy()
    #First case
    temp[2] = Points(0,0)
    result1 = IfTriangle(temp,0)
    #Second case
    temp1 = temp.copy()
    temp1[1] = triangle[2]
    result2 = IfTriangle(temp1,0)
    #Third case
    temp2 = temp1.copy()
    temp2[0] = triangle[1]
    result3 = IfTriangle(temp2,0)
    if result == result1 + result2 + result3:
        print("Origin is inside!")
    else:
        print("Origin not inside!")
        
def Fill(triangle):
    x = float(input()) 
    y = float(input())
    triangle.append( Points(x,y) ) 
    
    
if __name__ == "__main__":
    triangle = []
    for i in range(3):
        print("Enter point:")
        Fill(triangle)
    print("Is triangle?")
    IfTriangle(triangle,1)
    if IfTriangle(triangle,0) != 0:
        print("Is origin inside?")
        OriginIncluded(triangle)
    