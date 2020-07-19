class square:
    def __init__(self,side):
        self.side = side


    def areasq(self):
        return self.side ** 2
a=int(input("Enter the length of the side of square"))
obj=square(a)
print("The area of the square is",obj.areasq())


