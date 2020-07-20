class calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):

        return self.num1+self.num2

    def sub(self,num1,num2):
        return self.num1 - self.num2

    def mul(self,num1,num2):
        return self.num1 *self.num2

    def div(self,num1,num2):
        return self.num1 / self.num2
a=int(input("Enetr the first number "))
b=int(input("Enter the second number "))
obj=calculator(a,b)

k=obj.add()
l=obj.sub(a,b)
m=obj.mul(a,b)
n=obj.div(a,b)
print(k)
print(l)
print(m)
print(n)

