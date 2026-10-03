

class Rectangle:
    def __init__(self, L, W):
        self._Length = L
        self._Width = W

    def perimeter (self):
        return 2*(self._Length + self._Width)
    
    def Area (self):
        return self._Length * self._Width
    
R = Rectangle(12,10)
#print(f"perimeter: {R.perimeter()}")
#print (f"area: {R.Area()}")

R._Length = 20 #error in c++ but no error in python but wrong!
print(f"perimeter : {R.perimeter()}")
print(f"area : {R.Area()}")

        