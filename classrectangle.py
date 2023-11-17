class rectangle () :
    #def __init__(self) :
        #self.length = 10
        #self. width= 15

    def __init__(self,length, width) :
        self. length = length
        self.width =width
    

    #def __init__(self, newrectangle) :
        #self.length= newrectangle.length
        #self.width= newrectangle.width


    def perimeter(self):
        return (self.length + self.width)*2
    
    

    def area(self):
        return self.width + self.length
    

    def iscarre(self) :
        if self.width== self.length:
            return True
        else:
            return False
    

    def info(self):
        print (f"length of the rectangle is : {(self.length)}")
        print(f"width of the rectangls is:{(self.width)}")
        print(f"the perimeter of the rectsngle is:{(self.perimeter())}")
        print(f"the area of the rectangle is: {(self.area())}")
        print(f"it s a square:{(self.iscarre())}")

