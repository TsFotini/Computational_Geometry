#Exercise 2
import math
class Points:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Circle:
    def __init__(self,r):
        self.origin = Points(0,0)
        self.r = r
    def laticePoints(self):
        combinations = 4
        if self.r < 0:
            print("Error!Negative radius!")
            return -1;
        x = 1
        while x != self.r:
            square_Y = self.r*self.r - x*x
            y = math.sqrt(square_Y)
            if y.is_integer() == True:  #and y*y == square_Y
                combinations += 4
            x = x + 1
        return combinations
                
            
        
if __name__ == "__main__":
    print("Please enter the radius of the circle: ")
    rad = float(input())
    circle = Circle(rad)
    circle.laticePoints()
    print("Latice Points found:")
    lp = circle.laticePoints()
    print(lp)

