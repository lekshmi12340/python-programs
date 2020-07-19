class addrem():
    def __init__(self):
        self.m=[]
    def add(self,a):
        return self.m.append(a)

    def dis(self):
        return (self.m)

obj=addrem();

obj.add('Anu')
obj.add(1)
obj.add(3)



print(obj.dis())




